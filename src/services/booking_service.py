from typing import Iterable

from sqlalchemy import select

from database.models.bed_type import BedType
from database.models.booking import Booking
from database.models.customer import Customer
from database.models.invoice import Invoice
from database.models.room import Room, RoomType
from database.repositories.base_repository import Repository
from database.repositories.booking_repository import BookingRepository
from utils.singleton import singleton


@singleton
class BookingService:
    def __init__(self):
        self.booking_repo = BookingRepository[Booking]()

    def get_detail_booking(self):
        pass

    def get_infor_customer(self, phone):
        repo = Repository[Customer]()
        return repo.get(_filters=[
            Customer.phone == phone,
        ])

    def update_booking(self, booking):
        repo = Repository[Booking]()
        return repo.update(booking)

    def get_all_bookings(self):
        return Repository[Booking]().get_all()  # type: list[Booking]

    def get_room_by_id(self, customer_id):
        return Repository[Room]().get(_filters=[
            Customer.id == customer_id
        ])

    def get_all_type_bed(self):
        return Repository[BedType]().get_all()

    def get_all_type_room(self):
        return [member.value for member in RoomType]

    def filter_room(self, type_bed, type_room, price_min, price_max, num_of_customer, start_date, end_date) -> Iterable[
        Room]:
        a = self.booking_repo.filter_room(type_bed, type_room, price_min, price_max, num_of_customer,
                                          start_date,
                                          end_date)
        return a

    def create_booking(self, cus_id, type_booking, start_date, end_date, num_adult, num_child,
                       room_id):
        return self.booking_repo.create(Booking(
            customer_id=cus_id,
            booking_type=type_booking,
            start_date=start_date,
            end_date=end_date,
            num_adults=num_adult,
            num_children=num_child,
            room_id=room_id,
        ))

    def check_room_available(self, room_id, start_date, end_date):
        return self.booking_repo.check_room_available(room_id, start_date, end_date)

    def update_invoice(self, invoice):
        return Repository[Invoice]().update(invoice)
