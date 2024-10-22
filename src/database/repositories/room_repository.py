"""
Author: Nguyen Khac Trung Kien
"""

from typing import TypeVar
from database.models.room import Room
from database.repositories.base_repository import Repository
from utils.singleton import singleton


T = TypeVar('T')


class RoomRepository[T](Repository[T]):
    def __init__(self):
        super().__init__()

    def get_by_id(self , room_id ):
        return self.get(_filters=[
            Room.id == room_id
        ])
