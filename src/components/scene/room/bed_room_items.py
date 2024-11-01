from collections.abc import Iterable
from database.models.bed_room import BedRoom
from database.models.bed_type import BedType
from services.room_service import RoomService


from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QAction, QHBoxLayout, QLabel, QLineEdit, QMenu, QMessageBox, QPushButton, QToolButton, QVBoxLayout, QWidget


from typing import Callable

from components.scene.room.room_helpers import bed_type, get_bed_rooms
from utils.logging import app_logger


class ItemRow(QWidget):
    def __init__(self, bed_room: BedRoom, remove_callback : Callable, parent ):
        super().__init__(parent)
        self.bed_room = bed_room


        self.bed_type =   bed_type(self.bed_room.bed_type_id)


        # TODO: Check fetch able to get name form bed_type
        self.label = QLabel(str(self.bed_type.name), self)
        self.input = QLineEdit(self)
        self.input.setPlaceholderText('Enter number')
        self.input.setText(str(bed_room.bed_amount))  # Set default value
        self.input.setValidator(QDoubleValidator(0.99, 99.99, 2, self))  # Allow only numbers with up to 2 decimal places
        self.lblCapacity= QLabel(str(self.bed_type.capacity) + " Guests / Bed", self)

        # Create a button for deletion
        self.delete_button = QToolButton(self)
        self.delete_button.setText('Delete')
        self.delete_button.clicked.connect(remove_callback)

        # Connect input validation
        self.input.editingFinished.connect(self.validate_input)

        # Add widgets to layout
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.lblCapacity)
        self.layout.addWidget(self.delete_button)
        # self.parent.parentLayout.addRow(self.label, self.input, self.lblCapacity, self.delete_button)


    def get_bed_room_detail(self):
        """
        Return ( bed_type_name : bed_amount)
        """
        # TODO
        return self.bed_room


    def validate_input(self):
        # Validate the input number is greater than 0
        try:
            value = int(self.input.text())
            if value <= 0:
                raise ValueError
            # TODO
            self.bed_room.bed_amount = value
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Value must be greater than 0.")
            self.input.setText('1')  # Reset to default value if invalid
            self.input.setFocus()  # Set focus back to input


class BedRoomManager(QWidget):
    def __init__(self, room_id = None , parentLayout= None ):
        super().__init__()
        # All available type: Single, Double
        self.room_service  = RoomService()
        self.parentLayout = parentLayout

        self.bed_types: Iterable[BedType]= self.room_service .get_all_bed_types()
        self.room_id  = room_id
        # TODO
        # Bed room information before edit
        self.current_bed_rooms = get_bed_rooms(room_id = room_id )
        self.lookup_bed_type_to_bed_type_id  =  { str(bed_type.name) : bed_type.id for  bed_type  in self.bed_types}

        self.selected_bed_rooms : list[BedRoom] = []
        self.selected_item_widget : list[ItemRow] = []

        self.layout = QVBoxLayout(self)

        # Button to show available items
        self.add_button = QPushButton('Add room type', self)
        self.add_button.clicked.connect(self.show_item_menu)


        # Ensure at least one item exists at the start
        self._initUi()
        self._load_init_items()



    def _initUi(self):
        self.parentLayout.addWidget(self)
        self.layout.addWidget(self.add_button)
        self.setLayout(self.layout)


    def get_bed_details(self) -> list[BedRoom]:
        """
        Return a list of BedRoom not persistence to database
        BedRoom not set room_id yet
        """
        # bed_rooms= []
        # for item in self.selected_item_widget:
        #     bed_type_name  , amount = item.get_bed_room_detail()
        #     id  = self.lookup_bed_type_to_bed_type_id[bed_type_name]
        #     bed_rooms.append(BedRoom(bed_type_id = id , bed_amount = amount))
        return self.selected_bed_rooms
    def _load_init_items(self):
        if self.current_bed_rooms :
            for bed_room in self.current_bed_rooms:
                self.add_bed(bed_room)
        else:
            DEFAULT_BED_TYPE = self.bed_types[0] if self.bed_types   else None
            if DEFAULT_BED_TYPE:
                self.add_bed(DEFAULT_BED_TYPE)
            else:
                app_logger.warning("Cound not found any bed type")



    def show_item_menu(self):
        """
        Popup a list of selection when click to button
        """
        def bind_action(bed_type , parent):
            active_action = QAction(bed_type.name, parent)
            active_action.triggered.connect(lambda checked  , bed_type=bed_type: self.add_bed(bed_type))
            return active_action


        selected_bed_type_id   = set([bed_room.bed_type_id for bed_room in self.selected_bed_rooms])

        # Create and show the context menu
        menu = QMenu(self)
        for bed_type in self.bed_types:
            if bed_type.id not in selected_bed_type_id:
            # Use a default argument in the lambda to capture the current bed_type
                menu.addAction(bind_action(bed_type , self ))

        menu.exec(self.mapToGlobal(self.add_button.rect().bottomRight()))

    def add_bed(self, bed_type_or_bed_room  ):
        """
        From bed type add new bed_room of this bed_type when use click button add bed type
        Bed room is store information about room_id, bed_type_id and bed_amount
        """
        def add(bed_room: BedRoom):
            self.selected_bed_rooms.append(bed_room)
            item_row_widget = ItemRow(bed_room , lambda: self.remove_bed_room(item_row_widget, bed_room),  self)
            self.selected_item_widget.append(item_row_widget)
            self.layout.addWidget(item_row_widget)


        if isinstance(bed_type_or_bed_room, BedType):
            bed_room = BedRoom(bed_type_id= bed_type_or_bed_room.id, bed_amount = 1, room_id = self.room_id)
            add(bed_room)
        elif isinstance(bed_type_or_bed_room ,BedRoom):
            add(bed_type_or_bed_room)
        else: app_logger.warning("Unable to add item of unknow")
    def remove_bed_room(self, item_widget : QWidget, bed_room:  BedRoom):
        # Ensure at least one item remains
        MINIMUM_BED_TYPE  = 1
        if len(self.selected_bed_rooms) > MINIMUM_BED_TYPE :
            item_widget.deleteLater()  # Properly delete the widget
            self.selected_bed_rooms.remove(bed_room)  # Remove from selected items
            self.selected_item_widget.remove(item_widget)
        else:
            QMessageBox.warning(self, "Warning", "At least one item must remain.")