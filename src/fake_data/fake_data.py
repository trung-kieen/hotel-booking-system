"""
Author: Dang Xuan Lam
"""
import random
from datetime import datetime

from faker.proxy import Faker
from sqlalchemy.orm import create_session, Bundle, Session

from database.models.bed_room import BedRoom
from database.models.bed_type import BedType
from database.models.booking import Booking
from database.models.customer import Customer, Gender
from database.models.floor import Floor
from database.models.hotel import Hotel
from database.models.room import Room, RoomType

_session: Session
_ID_HOTEL = 1
room_types = [RoomType.Standard, RoomType.Deluxe, RoomType.Suit]
gender = [Gender.FEMALE, Gender.MALE]
_faker = Faker(["vi_VN"])


def fake(engine):
    global _session
    _session = create_session(bind=engine)
    _fake_hotel()
    _fake_floor()
    _fake_bed()
    _fake_room()
    _fake_customer()
    _fake_booking()


def _fake_booking():
    l_b = []
    for b_id in range(1, 10):
        s_date = _faker.date_time()
        stay_duration = random.randint(1, 10)
        l_b.append(
            Booking(
                id=b_id,
                customer_id=random.randint(1, 100),
                start_date=s_date,
                end_date=random.choice(
                    [None, _faker.date_between(start_date=s_date, end_date=datetime.now()) if s_date < datetime.now() else None]),
                num_adults=1,
                num_children=1,
                room_id=random.choice(range(1, 50)),
                is_canceled=False
            )
        )
    _session.add_all(l_b)
    _session.commit()


def _fake_customer():
    customers = []
    for customer_id in range(1, 100):
        customers.append(
            Customer(
                id=customer_id,
                firstname=_faker.first_name(),
                lastname=_faker.last_name(),
                address=_faker.address(),
                birth=_faker.date_of_birth(),
                gender=random.choice(gender),
                phone=_faker.phone_number(),
                email=_faker.email(),

            )
        )
    _session.add_all(customers)
    _session.commit()


def _fake_floor():
    _session.add_all([Floor(id=1, hotel_id=_ID_HOTEL),
                      Floor(id=2, hotel_id=_ID_HOTEL),
                      Floor(id=3, hotel_id=_ID_HOTEL),
                      Floor(id=4, hotel_id=_ID_HOTEL),
                      Floor(id=5, hotel_id=_ID_HOTEL)])
    _session.commit()


def _fake_room():
    room_id = 1
    for floor_id in range(1, 6):
        list_room = []
        beds_room = []
        min_price = 500  # Minimum price
        max_price = 2000  # Maximum price
        for _ in range(1, 11):
            list_room.append(
                Room(id=room_id, floor_id=floor_id, room_type=random.choice(room_types), is_locked=False,
                     price=random.randint(min_price, max_price)))
            beds_room.append(
                BedRoom(
                    bed_type_id=random.choice([1, 2, 3, 4]),
                    room_id=room_id,
                    bed_amount=1
                )
            )
            room_id += 1
        _session.add_all(list_room)
        _session.commit()
        _session.add_all(beds_room)
        _session.commit()


def _fake_hotel():
    h = Hotel(id=_ID_HOTEL, name="Khach san cua tui va iem", address=_faker.address(), phone=_faker.phone_number())
    _session.add(h)
    _session.commit()


def _fake_bed():
    # Add bed types data
    bed = [BedType(id=1, name="Single Bed", capacity=1),
           BedType(id=2, name="Double Bed", capacity=2),
           BedType(id=3, name="King Bed", capacity=2),
           BedType(id=4, name="Queen Bed", capacity=2)]

    # Add the objects to the session
    _session.add_all(bed)

    # Commit the session to save the data to the database
    _session.commit()
