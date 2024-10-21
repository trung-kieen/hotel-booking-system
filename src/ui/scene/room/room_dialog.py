
import sys
from typing import List
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QPushButton, QMenu, QAction, QToolBox,
    QVBoxLayout, QWidget, QLabel, QLineEdit, QToolButton, QMessageBox, QHBoxLayout
)
from enum import Enum

from sqlalchemy.sql.functions import grouping_sets
from database.models import bed_type
from database.models.bed_room import BedRoom
from database.models.bed_type import BedType
from database.models.room import Room, RoomType
from database.orm import Session
from database.repositories.base_repository import Repository
from services.room_service import ComboboxFilterAdapter, FormComboboxAdapter, bed_types, floor_members, room_type_members
from ui.ui_room_dialog import  Ui_Dialog
from PyQt5 import QtCore, QtWidgets

class FormAction (Enum):
    ADD   = 1 ,
    EDIT =  2  ,


class RoomDialog( QDialog):
    def __init__(self, room_id  = None ):
        super().__init__()
        # QMainWindow().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.floor_cmb= FormComboboxAdapter(floor_members( prefix= "") , self.ui.cmbFloor  )
        self.room_type_cmb = FormComboboxAdapter(room_type_members() , self.ui.cmbRoomType)
        self.room_id = room_id
        self.room:  Room
        self.form_action = FormAction.EDIT  if room_id  else FormAction.ADD
        # self.buttonBox.accepted.connect(self.add_customer) # type: ignore
        self.ui.buttonBox.accepted.connect(self.add_room)
        if self.form_action == FormAction.EDIT:
            self.ui.lbRoomId.setText(f"Room #{room_id}")
        else:
            self.room = Room()
            pass
            # TODO: Create room model if ADD mod

        self._load_room_by_room_id();



        # Create an instance of ItemManager
        self.item_manager = ItemManager()
        self.setLayout(self.ui.formLayout)
        self.ui.formLayout.addWidget(self.item_manager)

            # Load room by id
            # Populate data into form



        # Bing event save and save data for model

    def get_room_details(self)-> Room:
        room_type = self.room_type_cmb.current_key()
        price = float(self.ui.txtPrice.text())
        floor_id = self.floor_cmb.current_key()
        is_locked = self.ui.ckLockRoom.isChecked()
        new_room =  Room(floor_id=floor_id, room_type=room_type, is_locked=is_locked,price=price)
        return new_room
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
            session.rollback()  # Rollback in case of an error
            print(f"An error occurred: {e}")

        finally:
            session.close()  # Close the session



    def _load(self):
        if self.form_action  == FormAction.EDIT:
            self._load_room_by_room_id()
    def _load_room_by_room_id(self):
        """
        Load from model in field in form
        Use when user want to edit a room
        """
        if self.room_id:
            self.room = Session().query(Room).filter_by(id = self.room_id).one()
            self.floor_cmb.set_by_key(self.room.floor_id)
            self.room_type_cmb.set_by_key(self.room.room_type.name)




class ItemRow(QWidget):
    def __init__(self, label_text, remove_callback, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)

        # Create label and input field
        self.label = QLabel(label_text, self)
        self.input = QLineEdit(self)
        self.input.setPlaceholderText('Enter number')
        self.input.setText('1')  # Set default value
        self.input.setValidator(QDoubleValidator(0.99, 99.99, 2, self))  # Allow only numbers with up to 2 decimal places

        # Create a button for deletion
        self.delete_button = QToolButton(self)
        self.delete_button.setText('Delete')
        self.delete_button.clicked.connect(remove_callback)

        # Connect input validation
        self.input.editingFinished.connect(self.validate_input)

        # Add widgets to layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.delete_button)
    def get_bed_room_detail(self):
        """
        Return ( bed_type_name : bed_amount)
        """
        # TODO
        return (self.label.text(),   int(self.input.text()))


    def validate_input(self):
        # Validate the input number is greater than 0
        try:
            value = float(self.input.text())
            if value <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Value must be greater than 0.")
            self.input.setText('1')  # Reset to default value if invalid
            self.input.setFocus()  # Set focus back to input

class ItemManager(QWidget):
    def __init__(self, bed_type_to_amount = None ):
        super().__init__()
        # All available type: Single, Double

        self.bed_types: List[BedType]= bed_types()
        self.bed_type_to_amount = bed_type_to_amount
        self.lookup_bed_type_to_bed_type_id  =  { str(bed_type.name) : bed_type.id for  bed_type  in self.bed_types}

        self.selected_items : list[str] = []
        self.selected_rows : list[ItemRow] = []


        self.layout = QVBoxLayout(self)

        # Button to show available items
        self.add_button = QPushButton('Add room type', self)
        self.add_button.clicked.connect(self.show_item_menu)

        self.layout.addWidget(self.add_button)
        self.setLayout(self.layout)

        # Ensure at least one item exists at the start
        self._load_init_items()





    def get_bed_details(self) -> list[BedRoom]:
        """
        Return a list of BedRoom not persistence to database
        BedRoom not set room_id yet
        """
        bed_rooms= []
        for item in self.selected_rows:
            bed_type_name  , amount = item.get_bed_room_detail()
            id  = self.lookup_bed_type_to_bed_type_id[bed_type_name]
            bed_rooms.append(BedRoom(bed_type_id = id , bed_amount = amount))
        return bed_rooms
    def _load_init_items(self):
        if self.bed_type_to_amount:
            for bed_type , amount in self.bed_type_to_amount:
                self.add_item(bed_type , amount )

        else:
            self.add_item(self.bed_types[0].name)

    def show_item_menu(self):
        # Create and show the context menu
        menu = QMenu(self)

        all_bed_type = [str(bed_type.name)  for bed_type in self.bed_types]

        for item in all_bed_type:
            # Only show unselected items
            if item not in self.selected_items:
                action = QAction(item, self)
                action.triggered.connect(lambda checked, item=item: self.add_item(item))
                menu.addAction(action)

        menu.exec_(self.mapToGlobal(self.add_button.rect().bottomLeft()))

    def add_item(self, item , amount = 1):
        self.selected_items.append(item)
        item_row = ItemRow(item, lambda: self.remove_item(item_row), self)
        self.selected_rows.append(item_row)
        self.layout.addWidget(item_row)

    def remove_item(self, item_widget):
        # Ensure at least one item remains
        MINIMUM_BED_TYPE  = 0
        if len(self.selected_items) > MINIMUM_BED_TYPE :
            item_widget.deleteLater()  # Properly delete the widget
            self.selected_items.remove(item_widget.label.text())  # Remove from selected items
            self.selected_rows.remove(item_widget)
        else:
            QMessageBox.warning(self, "Warning", "At least one item must remain.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Available items for the popup menu

        # Set the main window properties
        self.setCentralWidget(self.item_manager)
        self.setWindowTitle('Item Manager')
        self.setGeometry(300, 300, 400, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
