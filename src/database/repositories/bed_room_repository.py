"""
Author: Nguyen Khac Trung Kien
Database interaction with model BedRoom
"""

from collections.abc import Iterable
from typing import TypeVar

from database.models import bed_room, bed_type
from database.models.bed_room import BedRoom
from database.repositories.base_repository import Repository


T = TypeVar('T')


class BedRoomRepository[T](Repository[T]):
    def __init__(self):
        super().__init__()


    def get_all_by_room_id(self, room_id ) -> Iterable[BedRoom]:
        return self.session.query(BedRoom).filter_by(room_id = room_id).all()
    def get_all_bed_id_by_room_id(self , room_id ):
        bed_rooms_by_room_id = self.get_all_by_room_id(room_id )
        return [ bed.id for bed in bed_rooms_by_room_id]

    def delete(self, item: T) -> None:
        self.delete(item)
    def delete_by_room_id(self,room_id ) -> None:
        self.session.query(BedRoom).filter_by(room_id= room_id ).delete()
        self.session.commit()
    def all_add(self ,  bed_rooms :Iterable):
        self.session.add_all(bed_rooms)
        self.session.commit()

    def delete_by_room_id_and_bed_type(self, room_id ,  bed_type_id ) -> None:
        self.session.query(BedRoom).filter_by(room_id = room_id  , bed_type_id = bed_type_id).delete()
