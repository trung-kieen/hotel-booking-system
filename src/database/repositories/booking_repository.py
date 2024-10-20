from database.models.booking import Booking
from database.repositories.base_repository import Repository


class BookingRepository(Repository[Booking]):
    def __init__(self):
        super().__init__()
    