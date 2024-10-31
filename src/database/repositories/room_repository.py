"""
Author: Nguyen Khac Trung Kien
"""

from typing import TypeVar
from database.models.room import Room
from database.repositories.base_repository import Repository
from utils.singleton import singleton


T = TypeVar('T')


class RoomRepository(Repository[T]):
    def __init__(self):
        super().__init__()

    def get_by_id(self , room_id ):
        return self.get(_filters=[
            Room.id == room_id
        ])
    def delete_by_id(self , room_id ) -> None:
        self.session.query(Room).filter_by(id = room_id).delete()
        self.session.commit()

    def count_not_locked(self):
        return self.session.query(Room).filter_by(is_locked  = False).count()


    def count(self):
        return self.session.query(Room).count()
