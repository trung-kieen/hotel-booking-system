"""
Author: Dang Xuan Lam
"""
import random
from datetime import datetime, timedelta

from components.messagebox.popup import ErrorPopup
from database.engine import EngineHolder
from faker.proxy import Faker
from sqlalchemy.orm import create_session, Bundle, Session

from database.models.bed_room import BedRoom
from database.models.bed_type import BedType
from database.models.booking import Booking
from database.models.customer import Customer, Gender
from database.models.floor import Floor
from database.models.hotel import Hotel
from database.models.invoice import Invoice, PaymentStatus
from database.models.room import Room, RoomType
from database.models.service import Service
from database.models.booking_service import BookingService
from database.repositories.base_repository import Repository

_session: Session
_ID_HOTEL = 1
room_types = [RoomType.Standard, RoomType.Deluxe, RoomType.Suit]
gender = [Gender.FEMALE, Gender.MALE]
_faker = Faker(["vi_VN"])


def fake(engine = EngineHolder().get_engine()):
    global _session
    _session = create_session(bind=engine)
    _fake_hotel()
    _fake_floor()
    _fake_bed()
    _fake_room()
    _fake_customer()
    _fake_services()
    _fake_booking()


def _fake_booking():
    l_b = []
    invoice_count = 1
    num_bookings = 100  # Tổng số lượng booking
    num_future_bookings = 20  # Số lượng booking đặt trước

    for b_id in range(1, num_bookings + 1):
        # Xác định ngày bắt đầu ngẫu nhiên
        if b_id <= num_bookings - num_future_bookings:
            # Booking đã thực hiện (ngày bắt đầu trong quá khứ)
            s_date = _faker.date_this_year(before_today=True, after_today=False)
        else:
            # Booking đặt trước (ngày bắt đầu trong tương lai)
            s_date = _faker.date_this_year(before_today=False, after_today=True)

        # Đảm bảo là không bị hủy để xét trường hợp đã check-in
        is_canceled = random.choice([False, True]) if b_id > (
                num_bookings - num_future_bookings) else False  # Đặt trước không bị hủy

        if is_canceled:
            # Nếu booking bị hủy
            l_b.append(
                Booking(
                    id=b_id,
                    customer_id=random.randint(1, 100),
                    start_date=s_date,  # Lưu ngày bắt đầu
                    checkin=None,
                    checkout=None,
                    end_date=s_date,  # Ngày kết thúc là ngày bắt đầu
                    num_adults=random.randint(1, 3),  # Số lượng người lớn ngẫu nhiên
                    num_children=random.randint(0, 2),  # Số lượng trẻ em ngẫu nhiên
                    room_id=random.choice(range(1, 100)),
                    is_canceled=True  # Đánh dấu là bị hủy
                )
            )
        else:
            # Nếu booking không bị hủy
            today = datetime.now().date()  # Lấy ngày giờ hiện tại (chỉ lấy phần ngày)

            if s_date > today:
                # Nếu ngày bắt đầu trong tương lai, thì chưa check-in
                checkin_time = None
                checkout_time = None
                end_date = s_date  # Ngày kết thúc bằng ngày bắt đầu
            else:
                # Nếu booking không bị hủy và đã xảy ra hoặc đang diễn ra
                checkin_time = _faker.date_time_between_dates(
                    datetime_start=datetime(s_date.year, s_date.month, s_date.day, 0, 0),
                    datetime_end=datetime(s_date.year, s_date.month, s_date.day, 23, 59)
                )

                # Tạo thời gian checkout
                stay_duration = random.randint(1, 10)  # Số ngày lưu trú ngẫu nhiên
                end_date = checkin_time + timedelta(days=stay_duration)  # Ngày kết thúc của booking

                if today <= end_date.date():  # Khách vẫn ở hoặc vừa check-out
                    checkout_time = None  # Không có checkout nếu khách vẫn ở
                else:
                    checkout_time = _faker.date_time_between_dates(
                        datetime_start=datetime(end_date.year, end_date.month, end_date.day, 8, 0),
                        datetime_end=datetime(end_date.year, end_date.month, end_date.day, 12, 0)
                    )

            # Thêm thông tin đặt phòng vào danh sách
            l_b.append(
                Booking(
                    id=b_id,
                    customer_id=random.randint(1, 100),
                    start_date=s_date,  # Lưu ngày bắt đầu
                    checkin=checkin_time,
                    checkout=checkout_time,  # Có thể là None nếu khách vẫn ở
                    end_date=end_date,  # Ngày kết thúc
                    num_adults=random.randint(1, 3),  # Số lượng người lớn ngẫu nhiên
                    num_children=random.randint(0, 2),  # Số lượng trẻ em ngẫu nhiên
                    room_id=random.choice(range(1, 100)),
                    is_canceled=False  # Đánh dấu là không bị hủy
                )
            )

            # Create a single invoice for this booking
            services = random.sample(_session.query(Service).all(), random.randint(1, 3))  # Random services
            total_price = sum(s.price for s in services) + Repository[Room]().get(_filters=[
                (Room.id == l_b[-1].room_id)
            ]).price if len(
                l_b) > 0 else 0

            # Link services to the invoice
            for service in services:
                _session.add(BookingService(
                    service_id=service.id,
                    booking_id=b_id,
                    quantity=random.randint(1, 5)  # Random quantity for each service
                ))

            invoice = Invoice(
                id=invoice_count,
                total_price=total_price,
                booking_id=b_id,  # Link the invoice to the booking
            )
            now = datetime.now()
            five_years_ago = now - timedelta(days=5*365)  # Approximation for 5 years

            invoice.created_at =  _faker.date_time_between(start_date=five_years_ago, end_date=now)
            _session.add(invoice)
            invoice_count += 1
            if not is_canceled:
                invoice.status = PaymentStatus.Done
    # Lưu vào session và commit
    _session.add_all(l_b)
    _session.commit()


def _generate_unique_cccd(existing_cccds):
    while True:
        # Tạo số CCCD gồm 12 chữ số
        cccd = str(random.randint(100000000000, 999999999999))
        if cccd not in existing_cccds:  # Kiểm tra xem số đã tồn tại chưa
            existing_cccds.add(cccd)  # Thêm số vào tập hợp
            return cccd


def _generate_cccds(num):
    existing_cccds = set()  # Tập hợp để lưu trữ các số CCCD đã tạo
    cccd_list = []

    for _ in range(num):
        cccd_list.append(_generate_unique_cccd(existing_cccds))

    return cccd_list


def _fake_customer():
    customers = []
    cccds = _generate_cccds(201)
    for customer_id in range(1, 200):  # Tăng số lượng khách hàng giả lên 200
        cur = random.randint(1, len(cccds) - 1)
        customers.append(
            Customer(
                id=customer_id,
                uuid=cccds[cur],
                firstname=_faker.first_name(),
                lastname=_faker.last_name(),
                address=_faker.address(),
                birth=_faker.date_of_birth(),
                gender=random.choice(gender),
                phone=_faker.phone_number(),
                email=_faker.email(),
            )
        )
        cccds.pop(cur)
    _session.add_all(customers)
    _session.commit()


def _fake_floor():
    for floor_id in range(1, 11):
        _session.add(Floor(id=floor_id, hotel_id=_ID_HOTEL))
    _session.commit()


def _fake_room():
    room_id = 1
    for floor_id in range(1, 11):
        list_room = []
        beds_room = []
        # Các thông số cho giá tối thiểu và tối đa
        min_price = 500  # Minimum price
        max_price = 2000  # Maximum price

        for _ in range(1, 11):  # Tạo 10 phòng mỗi tầng
            # Số lượng giường ngẫu nhiên (từ 1 đến 4)
            num_beds = random.randint(1, 4)
            # Chọn một loại phòng ngẫu nhiên
            room_type = random.choice(room_types)
            # Tính toán giá dựa trên loại phòng và số lượng giường
            price = random.randint(min_price, max_price) * num_beds // 2

            # Tạo phòng với các thuộc tính phù hợp
            room = Room(id=room_id, floor_id=floor_id, room_type=room_type, is_locked=False, price=price)
            list_room.append(room)

            # Tạo giường cho phòng
            for _ in range(num_beds):
                beds_room.append(
                    BedRoom(
                        bed_type_id=random.choice([1, 2, 3, 4]),  # Chọn loại giường ngẫu nhiên
                        room_id=room_id,
                        bed_amount=1  # Mỗi giường chỉ tính 1
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


_SERVICE_NAMES = [
    "Laundry Service",  # Dịch vụ giặt là
    "Spa",  # Dịch vụ spa
    "Gym",  # Dịch vụ phòng gym
    "Swimming Pool",  # Dịch vụ bể bơi
    "Airport Shuttle",  # Dịch vụ đưa đón sân bay
    "Car Rental",  # Thuê xe
    "Massage",  # Dịch vụ massage
    "Restaurant",  # Dịch vụ nhà hàng
    "Bar",  # Dịch vụ quầy bar
]

_NUM_SERVICES = 10


def _fake_services():
    services = []

    for _ in range(_NUM_SERVICES):
        service = Service(
            name=random.choice(_SERVICE_NAMES),
            price=random.uniform(50, 500)
        )
        services.append(service)

    # Thêm vào session và commit
    _session.add_all(services)
    _session.commit()
