"""
Author: Dang Xuan Lam
"""
from typing import Iterable

from sqlalchemy import select, func, and_, or_
from sqlalchemy.orm import aliased, joinedload
from typing_extensions import TypeVar

from database.models.bed_room import BedRoom
from database.models.bed_type import BedType
from database.models.booking import Booking
from database.models.room import Room
from database.repositories.base_repository import Repository

T = TypeVar('T')


class BookingRepository[T](Repository[T]):
    def __init__(self):
        super().__init__()

    def filter_room(self, type_bed, type_room, price_min, price_max, num_of_customer, start_date, end_date) -> Iterable[
        Room]:
        bed_capacity_subquery = (
            select(func.sum(BedType.capacity).label('total_capacity'))
            .select_from(BedType)
            .join(BedRoom, BedType.id == BedRoom.bed_type_id)
            .where(BedRoom.room_id == Room.id)
            .scalar_subquery()
        )

        _filter = [
            Room.bed_types.any(BedType.name == type_bed),
            Room.room_type == type_room,
            Room.is_locked == False,
            bed_capacity_subquery >= num_of_customer
        ]

        if price_min != 0:
            _filter.append(Room.price >= price_min)
        if price_max != 0:
            _filter.append(Room.price <= price_max)
        with self.session.no_autoflush:
            query = (
                self.session.query(Room)
                .outerjoin(Booking, Booking.room_id == Room.id)
                .options(joinedload(Room.bed_types), joinedload(Room.bookings))
                .filter(and_(
                    or_(
                        Booking.id == None,
                        Booking.is_canceled == True,
                        and_(
                            Booking.is_canceled == False,
                            or_(
                                Booking.start_date >= end_date,
                                Booking.end_date <= start_date
                            )
                        )
                    ),
                    *_filter
                ))
                .distinct()
            )
            rooms = query.all()

            # Manually add the queried rooms and bookings to the session if necessary
            for room in rooms:
                if room not in self.session:
                    self.session.add(room)
                for booking in room.bookings:
                    if booking not in self.session:
                        self.session.add(booking)

        return rooms

    def create(self, booking):
        self.session.add(booking)
        self.session.commit()
        return booking

    def check_room_available(self, room_id, start_date, end_date):
        availability_query = (
            self.session.query(Room)
            .outerjoin(Booking, Booking.room_id == Room.id)
            .filter(Room.id == room_id)
            .filter(
                or_(
                    Booking.id == None,  # Phòng không có booking nào
                    and_(
                        Booking.is_canceled == True,  # Phòng có booking nhưng đã bị hủy
                        or_(
                            Booking.start_date >= end_date,
                            Booking.end_date <= start_date
                        )
                    ),
                    and_(
                        Booking.is_canceled == False,  # Chỉ kiểm tra booking chưa hủy
                        or_(
                            Booking.start_date >= end_date,
                            Booking.end_date <= start_date
                        )
                    )
                )
            )
            .distinct()
        )

        return availability_query.count() > 0

    def filter_booking(self, filters=None):
        query = self.session.query(Booking).join(Booking.customer)

        if filters:
            query = query.filter(*filters)

        return query.options(joinedload(Booking.customer)).all()
