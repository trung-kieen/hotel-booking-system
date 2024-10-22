
import sys
from typing import List
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import (
     QDialog
)

from PyQt5 import QtCore
from enum import Enum

from sqlalchemy import except_

from database.models.room import Room
from database.orm import Session
from services.room_service import  FormComboboxAdapter, BedRoomManager, RoomService, bed_types, floor_members, room_type_members
from ui.ui_room_dialog import  Ui_Dialog

class FormAction (Enum):
    ADD   = 1 ,
    EDIT =  2  ,


class RoomDialog( QDialog):
    def __init__(self, room_id  = None ):
        """
        Input room_id for edit room information
        Otherwise for add new room
        """
        super().__init__()
        self.room_id = room_id
        self.form_action = FormAction.EDIT  if room_id  else FormAction.ADD
        self.service = RoomService();


        # Boot strap component
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.floor_cmb= FormComboboxAdapter(floor_members() , self.ui.cmbFloor  )
        self.room_type_cmb = FormComboboxAdapter(room_type_members() , self.ui.cmbRoomType)
        self.bed_room_manager = BedRoomManager(room_id, parentLayout = self.ui.formLayout)



        self.load_form()
        self._register_event()



    def _register_event(self):
        if self.form_action == FormAction.ADD:
            self.ui.buttonBox.accepted.connect(self.add_room)
        elif  self.form_action == FormAction.EDIT:
            self.ui.buttonBox.accepted.connect(self.update_room)
    def get_room_details(self)-> Room:
        """
        Get current input as room object from orm `Room` base on form action:
        - Create new entity room and set value from form input
        - Load entity from persistence context => update value  from input form in entity without persistence yet
        Not emmit to load bed_room details because it is reference entity
        """
        if self.form_action == FormAction.ADD:

            room_type = self.room_type_cmb.current_key()
            price = float(self.ui.txtPrice.text())
            floor_id = self.floor_cmb.current_key()
            is_locked = self.ui.ckLockRoom.isChecked()

            room =  Room(floor_id=floor_id, room_type=room_type, is_locked=is_locked,price=price, id = self.room_id)
            return room
        elif self.form_action == FormAction.EDIT:
            room = self.service.get_room_by_id(self.room_id)

            # Get value from form to variable
            room_type = self.room_type_cmb.current_key()
            price = float(self.ui.txtPrice.text())
            floor_id = self.floor_cmb.current_key()
            is_locked = self.ui.ckLockRoom.isChecked()


            # Set value to entity object
            if room_type: room.room_type = room_type
            if price: room.price = price
            if floor_id: room.floor_id= floor_id
            if is_locked is not None: room.is_locked = is_locked
            return room

        else:
            print("Unalbe to load room")
            return None

    # TODO: Handle exception
    def update_room(self):
        """
        Use only when edit room
        """

        if self.form_action != FormAction.EDIT: return
        session = Session()
        try:
            updated_room = self.get_room_details()
            self.service.update_room(updated_room)
            # Need to persistence room before to get new room id
            session.commit()

            bed_type_ids_before = set(bed_room.bed_type_id for bed_room in  self.service.get_all_bed_by_room_id(self.room_id))


            bed_rooms = self.bed_room_manager.get_bed_details()
            bed_type_ids_after = set(bed.bed_type_id  for bed in bed_rooms) # After is get from form information

            added_bed_type_id = bed_type_ids_after - bed_type_ids_before
            updated_bed_type_id = bed_type_ids_after &  bed_type_ids_before
            deleted_bed_type_id =   bed_type_ids_before  -  bed_type_ids_after

            for type_id in deleted_bed_type_id:
                self.service.delete_bed_room_by_room_id_and_bed_type(self.room_id  , type_id)
            for bed  in bed_rooms:
                if bed.bed_type_id in added_bed_type_id:
                    session.add(bed)
                elif bed.bed_type_id in updated_bed_type_id:
                    self.service.update_bed_room(bed)
            session.commit()

        except Exception as e:
            session.rollback()
            print(f"Error occurred when try to update room and bed room: {e}")

        finally:
            session.close()
    def add_room(self):
        if self.form_action != FormAction.ADD: return
        session = Session()
        try:
            new_room = self.get_room_details()
            session.add(new_room)
            # Need to persistence room before to get new room id
            session.commit()

            for bed in self.bed_room_manager.get_bed_details():
                bed.room_id = new_room.id
                session.add(bed)

            session.commit()

        except Exception as e:
            session.rollback()
            print(f"Error occurred when try to add room and bed room: {e}")

        finally:
            session.close()



    def load_form(self):
        """
        Load data to room information to form
        """
        try:
            # Work if exist room information
            if self.room_id:
                self.ui.lbRoomId.setText(f"Room #{self.room_id}")
                room  = self.service.get_room_by_id(self.room_id)
                self.floor_cmb.set_by_key(room.floor_id)
                self.room_type_cmb.set_by_key(room.room_type.name)
                self.ui.txtPrice.setText("{:.0f}".format(room.price ))
            else:
                self.ui.lbRoomId.setText(f"New room")
        except Exception as ex:
            print("Unable to load room details ")
