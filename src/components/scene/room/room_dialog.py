"""
Author: Nguyen Khac Trung Kien
"""
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (
     QDialog
)

from enum import Enum


from database.models.room import Room
from services.room_service import  RoomService
from components.scene.room.bed_room_items import BedRoomManager
from components.scene.room.combobox_manager import FormComboboxAdapter
from components.scene.room.room_helpers import floor_members, room_type_members
from ui.ui_room_dialog import  Ui_Dialog
from utils.decorator import handle_exception

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
        self.room_service = RoomService();


        # Boot strap component
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.floor_cmb= FormComboboxAdapter(floor_members() , self.ui.cmbFloor  )
        self.room_type_cmb = FormComboboxAdapter(room_type_members() , self.ui.cmbRoomType)
        self.bed_room_manager = BedRoomManager(room_id, parentLayout = self.ui.formLayout)
        self._init_ui()



        self.load_form()
        self._register_event()


    def _init_ui(self):
        self.ui.txtPrice.setValidator(QIntValidator(0, 100000000, self))

    def _register_event(self):
        self.ui.txtPrice.textChanged.connect(
            lambda: self.ui.txtPrice.setText('0') if self.ui.txtPrice.text().strip() == "" else None)
    def get_room_details(self)-> Room:
        """
        Get current input as room object from orm `Room` base on form action:
        - Create new entity room and set value from form input
        - Load entity from persistence context => update value  from input form in entity without persistence yet
        Not emmit to load bed_room details because it is reference entity
        """

        room_type = self.room_type_cmb.current_key()
        price = float(self.ui.txtPrice.text())
        floor_id = self.floor_cmb.current_key()
        is_locked = self.ui.ckLockRoom.isChecked()

        # ORM deal with room without id as new room to insert and merge/update room if room already have id
        room =  Room(floor_id=floor_id, room_type=room_type, is_locked=is_locked,price=price, id = self.room_id)
        return room



    @handle_exception
    def accept(self):
        """
        Override default action when dialog form submit to perform database write action and validate data
        Any violation with database constraint will raise exception
        `@handle_exception` watch exception and return message to user avoid interrupt program
        Form will not submit if exception throw
        """
        if self.form_action == FormAction.ADD:
            self.add_room()
        else:
            self.update_room()
        super().accept()

    def update_room(self):
        """
        Use only when edit room
        """
        self.room_service.update_room_and_bed(self.get_room_details(), self.bed_room_manager.get_bed_details())


    def add_room(self):
        self.room_service.add_room_and_bed(self.get_room_details(), self.bed_room_manager.get_bed_details())




    @handle_exception
    def load_form(self):
        """
        Load display room data from database to dialog form
        """
        # Work if exist room information
        if self.room_id:
            # Get data from database
            room  = self.room_service.get_room_by_id(self.room_id)


            # Load model to form
            self.ui.lbRoomId.setText(f"Room #{self.room_id}")
            self.floor_cmb.set_by_key(room.floor_id)
            self.room_type_cmb.set_by_key(room.room_type.name)
            self.ui.txtPrice.setText("{:.0f}".format(room.price ))
        else:
            self.ui.lbRoomId.setText(f"New room")
            DEFAULT_PRICE =  1000
            self.ui.txtPrice.setText(str(DEFAULT_PRICE))
