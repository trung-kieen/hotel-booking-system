"""
Author: Nguyen Khac Trung Kien
"""
from collections.abc import Iterable
from typing import Any, Callable, List, Tuple, overload

from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QAction, QComboBox, QHBoxLayout, QLabel, QLineEdit, QMenu, QMessageBox, QPushButton, QToolButton, QVBoxLayout, QWidget
from database.models import bed_room
from database.models import bed_type
from database.models.bed_room import BedRoom
from database.models.bed_type import BedType
from database.models.floor import Floor
from database.models.room import Room, RoomType
from database.orm import Session
from database.repositories import bed_room_repository, room_repository
from database.repositories.base_repository import Repository
from database.repositories.bed_room_repository import BedRoomRepository
from database.repositories.bed_type_repository import BedTypeRepository
from database.repositories.room_repository import RoomRepository
from utils.decorator import transaction
from utils.singleton import singleton


@singleton
class RoomService:
    def __init__(self):
        self.room_repo = RoomRepository[Room]()
        self.bed_type_repo = BedTypeRepository[BedType]()
        self.bed_room_repo : BedRoomRepository[BedRoom]= BedRoomRepository[BedRoom]()

    # def get_detail_booking(self):
    #     pass


    def update_room(self, room):
        return self.room_repo.update(room)
    def update_bed_room(self, bed_room):
        return self.bed_room_repo.update(bed_room)
    def add_bed_room(self , bed_room):
        self.bed_room_repo.insert(bed_room)

    def delete_room_by_id(self , room_id ):
        self.room_repo.delete_by_id(room_id)
    def get_all_rooms(self):
        return self.room_repo.get_all()

    def get_room_by_id(self, room_id):
        return self.room_repo.get_by_id(room_id)
    def get_all_bed_types(self ):
        return self.bed_type_repo.get_all_bed_types()


    def get_bed_type_by_id(self , bed_type_id ):
        return self.bed_type_repo.get_bed_type_by_id(bed_type_id)
    def get_all_bed_by_room_id(self , room_id) -> Iterable[BedRoom]:
        """
        Return a list of bed_id filter by bed room
        """
        return  self.bed_room_repo.get_all_by_room_id(room_id)


    def delete_bed_room_by_room_id_and_bed_type(self , room_id , type_id ) -> None :
        self.bed_room_repo.delete_by_room_id_and_bed_type(room_id , type_id)

    def save_bed_room_by_room_id (self , room_id   , bed_rooms : Iterable[BedRoom] ):

        # persisted_bed_rooms_id = set(self.bed_room_repo.get_all_bed_id_by_room_id(room_id))
        final_bed_rooms_id = set([room.id for room in bed_rooms])
        # list_add  = final_bed_rooms_id - persisted_bed_rooms_id
        # list_delete  = persisted_bed_rooms_id - final_bed_rooms_id
        # list_update = persisted_bed_rooms_id & final_bed_rooms_id
        # for bed in bed_rooms:
        #     # TODO
        #     if bed.id in list_add:
        #         self.bed_room_repo.insert(bed)
        #     if bed.id in list_update:
        #         self.bed_room_repo.update(bed)
        #     if bed.id in list_delete:
        #         self.bed_room_repo.delete_room_id(bed.id)

        for bed_room in bed_rooms:
            bed_room.room_id = room_id
        self.bed_room_repo.delete_by_room_id(room_id)
        self.bed_room_repo.insert_all(bed_rooms)

    @transaction
    def update_room_and_bed (self,  updated_room : Room , bed_rooms : Iterable[BedRoom], session =Session()):
        self.update_room(updated_room)
        # Need to persistence room before to get new room id
        session.commit()

        bed_type_ids_before = set(bed_room.bed_type_id for bed_room in  self.get_all_bed_by_room_id(updated_room.id))


        bed_type_ids_after = set(bed.bed_type_id  for bed in bed_rooms) # After is get from form information

        added_bed_type_id = bed_type_ids_after - bed_type_ids_before
        updated_bed_type_id = bed_type_ids_after &  bed_type_ids_before
        deleted_bed_type_id =   bed_type_ids_before  -  bed_type_ids_after

        for type_id in deleted_bed_type_id:
            self.delete_bed_room_by_room_id_and_bed_type(updated_room.id  , type_id)
        for bed  in bed_rooms:
            if bed.bed_type_id in added_bed_type_id:
                session.add(bed)
            elif bed.bed_type_id in updated_bed_type_id:
                self.update_bed_room(bed)

    @transaction
    def add_room_and_bed (self , new_room  : Room , bed_rooms : Iterable [ BedRoom], session= Session()):
        session.add(new_room)
            # Need to persistence room before to get new room id
        session.commit()

        for bed in bed_rooms:
            bed.room_id = new_room.id
            session.add(bed)



def bed_types() -> list[BedType]:
    """
    Return list of all available bed type in database
    """
    # TODO: use service instead to close session with singleton service
    bed_type  = Session().query(BedType).all()
    return bed_type




def bed_type( bed_type_id ) -> BedType:
    t = Session().query(BedType).filter_by(id = bed_type_id).first()
    return t


def get_bed_rooms( room_id ) -> Iterable[BedRoom]:
    """
    Return a list of bed room information in a room
    """
    if room_id:
        return Session().query(BedRoom).filter_by(room_id = room_id ).all()
    else:
        return []

def lock_members() -> Iterable:
    return [(0 , "Active"), (1 , "Locked" )]


def floor_members(prefix = "Floor ") -> Iterable:
    """
    Get floor key, view_value  from table to load into combobox
    Use to create `ComboboxFilter()`
    """
    floors = Repository[Floor]().get_all()

    members = [(floor.id  , prefix + str(floor.id) ) for floor in floors ]
    return members
def room_type_members() -> Iterable:
    """
    Get members(key, view_value) from Enum class define (not from table) to load in combobox
    Use to create `ComboboxFilter()`
    """
    return tuple((room.name , room.name) for room in RoomType)




class FormComboboxAdapter():
    def __init__(self, combobox_members: Iterable[Tuple[Any , Any]],cmb :  QComboBox ) -> None:
        """
        @combobox_members: list(key_value , view_value)
        key_value is value which will actually interact with database
        view_value is use to display information for human readable
        For example:
        Database room have room_type_id = key_value = 1 which reference to room_type.name = view_value = 'single'
        @cmb: actual combobox item to display in gui
        """
        self.combobox_members = combobox_members
        self.combobox : QComboBox = cmb
        self.set_items()
    def set_items(self):
        self.combobox.clear()
        self.combobox.addItems(self._get_items_view())

    def _get_items_view(self):
        """
        Return a list of view to display in combobox
        Example: ["Floor 1", "Floor 2", "Floor 3"]
        """
        view =  [view_value for key , view_value in self.combobox_members]
        return view
    def set_by_key(self , key ):
        key_idx = 0
        for k , v in self.combobox_members:
            if key ==  k:
                break;
            key_idx += 1
        self.combobox.setCurrentIndex(key_idx)



    def current_key(self):
        """
        Current select key_value for database interaction
        """
        for key , value in self.combobox_members:
            if self.combobox.currentText() == value:
                return key


class ComboboxFilterAdapter():
    """
    Use to load selection for a property in table as combobox
    Auto add items for default select `all_item_selection` like select all items exist
    Example:  Floor >: All, Floor 1, Floor 2, ...
    """
    def __init__(self, combobox_members: Iterable[Tuple[Any , Any]],cmb :  QComboBox , field_name :str , all_view_value = None) -> None:
        """
        field_name use for query condition
        """
        self.combobox_members = combobox_members
        self.combobox = cmb
        self.field_name = field_name
        self.all_view_value= all_view_value
        self.set_items()
    def _get_items_view(self):
        """
        Return a list of view to display in combobox
        Example: ["Floor 1", "Floor 2", "Floor 3"]
        """
        view =  [view_value for key , view_value in self.combobox_members]
        if self.all_view_value:
            view = [self.all_view_value ] + view
        return view
    def set_items(self):
        self.combobox.clear()
        self.combobox.addItems(self._get_items_view())

    def query_condition(self):
        """
        Return a predicate to express user select filter
        Example:
        User select item have text room_type = 'single'
        'single' is room_type.name for actually record of room_type_id = 1
        => return fitler as {"room_type_id" : 1}
        """
        key = self.current_key()
        if key != None:
            return {self.field_name :  key}
        # Key is none when filter for all value of this predicate => Make it always true
        else:
            return None


    def current_key(self):
        for key , value in self.combobox_members:
            if self.combobox.currentText() == value:
                return key


        return None





def query_condition_translator(*predicates) -> str :
    """
    Use to pass a list of combobox filter to change those filter selection to raw query
    :meth:`ComboboxFilter.query_condition()`
    Example:
    Input: ({'floor_id': 2}, {'room_type': 0})
    Output: floor_id = 2 AND room_type = 0
    """
    predicates = [x for x in predicates if x ] # Remove none value
    if not predicates:
        return "1 = 1"
    conditions = []
    for predicate in predicates:
        if predicate:
            for field_name , value in predicate.items():
                condition = field_name + " = "
                if type(value) is int:
                    condition += str(value)

                # Wrap for string, date value like WHERE name = 'abc' AND date = '2024-02-24'
                else:
                    condition += f"'{str(value)}'"
                conditions.append(condition)

    return " AND ".join(conditions)


class ItemRow(QWidget):
    def __init__(self, bed_room: BedRoom, remove_callback : Callable, parent ):
        super().__init__(parent)
        print("Add bed room " , bed_room.bed_type_id )
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
                print("Cound not found any bed type")



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
        else: print("Unable to add item of unknow")
    def remove_bed_room(self, item_widget : QWidget, bed_room:  BedRoom):
        # Ensure at least one item remains
        MINIMUM_BED_TYPE  = 1
        if len(self.selected_bed_rooms) > MINIMUM_BED_TYPE :
            item_widget.deleteLater()  # Properly delete the widget
            self.selected_bed_rooms.remove(bed_room)  # Remove from selected items
            self.selected_item_widget.remove(item_widget)
        else:
            QMessageBox.warning(self, "Warning", "At least one item must remain.")
