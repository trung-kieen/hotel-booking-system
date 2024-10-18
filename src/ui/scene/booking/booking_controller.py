from database.models.booking import Booking
from database.repositories.base_repository import Repository
from utils.singleton import singleton


@singleton
class BookingController:
    def __init__(self):
        self.bookings = []
        
    def add_booking(self, booking):
        pass
    def remove_booking(self, booking):
        pass
    def get_detail_bookings(self):
        pass
    def filter_bookings(self, bookings):
        pass
    def get_all_bookings(self):
        return Repository[Booking]().get_all()
        