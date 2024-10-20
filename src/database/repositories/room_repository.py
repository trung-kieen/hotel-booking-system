"""
Author: Nguyen Khac Trung Kien
"""

from typing import TypeVar
from database.repositories.base_repository import Repository
from utils.singleton import singleton


T = TypeVar("T")
@singleton
class RoomRepository[T](Repository[T]):
    """
    Example: floor = Repository[Floor]().get_all()
    """
    def __init__(self):
        super().__init__()
