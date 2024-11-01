"""
Author: Nguyen Khac Trung Kien
Database interaction with model BedType
"""

from typing import TypeVar

from database.models.bed_type import BedType
from database.repositories.base_repository import Repository
from utils.singleton import singleton


T = TypeVar('T')


class BedTypeRepository[T](Repository[T]):
    def __init__(self):
        super().__init__()

    def get_all_bed_types(self):
        return self.get_all()  # type: list[Booking]

    def get_bed_type_by_id(self, bed_type_id):
        return self.get(_filters=[
            BedType.id == bed_type_id
        ])
