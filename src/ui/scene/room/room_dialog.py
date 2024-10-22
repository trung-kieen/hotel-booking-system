
import sys
from typing import List
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import (
     QDialog
)
from enum import Enum

from database.models.room import Room
from database.orm import Session
from services.room_service import  FormComboboxAdapter, ItemManager, bed_types, floor_members, room_type_members
from ui.ui_room_dialog import  Ui_Dialog

class FormAction (Enum):
    ADD   = 1 ,
    EDIT =  2  ,


class RoomDialog( QDialog):
    def __init__(self, room_id  = None ):
        super().__init__()
        self.room_id = room_id


        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.floor_cmb= FormComboboxAdapter(floor_members( prefix= "") , self.ui.cmbFloor  )
        self.room_type_cmb = FormComboboxAdapter(room_type_members() , self.ui.cmbRoomType)

        # Model
        self.room:  Room
        self.form_action = FormAction.EDIT  if room_id  else FormAction.ADD

        # TODO Handle to add and edit separate
        if self.form_action == FormAction.ADD:
            self.room = Room()
            self.ui.buttonBox.accepted.connect(self.add_room)
        elif  self.form_action == FormAction.EDIT:
            self._load_room(self.room_id)
            self.ui.buttonBox.accepted.connect(self.update_room)
            self.ui.lbRoomId.setText(f"Room #{room_id}")




        # Create an instance of ItemManager
        self.item_manager = ItemManager()
        self.ui.formLayout.addWidget(self.item_manager)

            # Load room by id
            # Populate data into form



        # Bing event save and save data for model

    def get_room_details(self)-> Room:
        """
        Get current input as room object from orm
        """
        room_type = self.room_type_cmb.current_key()
        price = float(self.ui.txtPrice.text())
        floor_id = self.floor_cmb.current_key()
        is_locked = self.ui.ckLockRoom.isChecked()
        new_room =  Room(floor_id=floor_id, room_type=room_type, is_locked=is_locked,price=price)
        return new_room
    def update_room(self):
        # TODO
        pass
    def add_room(self):
        session = Session()
        try:
            new_room = self.get_room_details()
            session.add(new_room)
            # Need to persistence room before to get new room id
            session.commit()



            for bed in self.item_manager.get_bed_details():
                bed.room_id = new_room.id
                session.add(bed)

            session.commit()

        except Exception as e:
            session.rollback()
            print(f"Error occurred when try to add room and bed room: {e}")

        finally:
            session.close()



    def _load(self):
        if self.form_action  == FormAction.EDIT:
            self._load_room(self.room_id)
    def _load_room(self, room_id ):
        """
        Load from model in field in form
        Use when user want to edit a room
        """
        if room_id:
            self.room = Session().query(Room).filter_by(id = self.room_id).one()
            self.floor_cmb.set_by_key(self.room.floor_id)
            self.room_type_cmb.set_by_key(self.room.room_type.name)
        # TODO: load bed_type and amount
