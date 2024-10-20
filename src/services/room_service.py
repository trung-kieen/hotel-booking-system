"""
Author: Nguyen Khac Trung Kien
"""
from collections.abc import Iterable
from typing import Any, Tuple

from PyQt5.QtWidgets import QComboBox
from database.models.floor import Floor
from database.models.room import RoomType
from database.repositories.base_repository import Repository





def floor_members() -> Iterable:
    """
    Get floor key, view_value  from table to load into combobox
    Use to create `ComboboxFilter()`
    """
    floors = Repository[Floor]().get_all()

    members = [(floor.id  , "Floor " + str(floor.id) ) for floor in floors ]
    return members
def room_type_members() -> Iterable:
    """
    Get members(key, view_value) from Enum class define (not from table) to load in combobox
    Use to create `ComboboxFilter()`
    """
    return tuple((room.name , room.name) for room in RoomType)






class ComboboxFilter():
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
        return [self.all_view_value] + [view_value for key , view_value in self.combobox_members]
    def set_items(self):
       self.combobox.addItems(self._get_items_view())

    def query_condition(self):
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
