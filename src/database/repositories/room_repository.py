

from typing import TypeVar
from database.repositories.base_repository import Repository
from utils.singleton import singleton
from database.models.room import Room

T = TypeVar("T")
@singleton
class RoomRepository[T](Repository[T]):
    def __init__(self):
        super().__init__()
