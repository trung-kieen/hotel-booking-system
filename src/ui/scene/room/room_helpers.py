from database.models.bed_room import BedRoom
from collections.abc import Iterable
from database.models.bed_type import BedType
from database.models.floor import Floor
from database.models.room import RoomType
from database.orm import Session
from database.repositories.base_repository import Repository

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

