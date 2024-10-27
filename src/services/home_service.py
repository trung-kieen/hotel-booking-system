"""
Author: Nguyen Khac Trung Kien
"""
from collections.abc import Iterable
from typing import Any, Callable, List, Tuple, overload

from utils import query as custom_query
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QAction, QComboBox, QHBoxLayout, QLabel, QLineEdit, QMenu, QMessageBox, QPushButton, QToolButton, QVBoxLayout, QWidget
from database.engine import EngineHolder
from database.models import bed_room
from database.models import bed_type
from database.models.bed_room import BedRoom
from database.models.bed_type import BedType
from database.models.booking import Booking
from database.models.floor import Floor
from database.models.room import Room, RoomType
from database.orm import Session
from database.repositories import bed_room_repository, room_repository
from database.repositories.base_repository import Repository
from database.repositories.bed_room_repository import BedRoomRepository
from database.repositories.bed_type_repository import BedTypeRepository
from database.repositories.booking_repository import BookingRepository
from database.repositories.room_repository import RoomRepository
from utils.decorator import handle_exception, transaction
from utils.singleton import singleton


@singleton
class HomeService:
    def __init__(self):
        self.room_repo = RoomRepository[Room]()
        self.bed_type_repo = BedTypeRepository[BedType]()
        self.bed_room_repo : BedRoomRepository[BedRoom]= BedRoomRepository[BedRoom]()
        self.booking_repo : BookingRepository[Booking] =  BookingRepository[Booking]()

    def total_working_rooms(self):
        return self.room_repo.count_not_locked()
    def total_rooms(self):
        return self.room_repo.count()
    def total_customers(self):
        return int(EngineHolder().scalar("SELECT COUNT(*) from customers"))
    def total_booking(self):
        return int(EngineHolder().scalar("SELECT COUNT(*) from bookings"))
    def total_success_booking(self):
        return int(EngineHolder().scalar("SELECT COUNT(*) from bookings WHERE is_canceled = FALSE"))
    def total_canceled_booking(self):
        return int(EngineHolder().scalar("SELECT COUNT(*) from bookings WHERE is_canceled = TRUE"))


    def income_by_month(self):
        r = EngineHolder().all(custom_query.query_invoice_total_group_by_period , period = 'm' )
        return extract_period_from_result_set(r)

    def income_by_quater(self):
        r = EngineHolder().all(custom_query.query_invoice_total_group_by_period , period = 'q' )
        return extract_period_from_result_set(r)
    def income_by_year(self):
        r = EngineHolder().all(custom_query.query_invoice_total_group_by_period , period = 'y' )
        return extract_period_from_result_set(r)
    def today_booking_by_status(self):
        return EngineHolder().all(custom_query.query_today_booking_status, period = 'y' )



def extract_period_from_result_set(rs, expect_labels: Iterable | None = None):
    """
    Input:
    [(Q1, 24), (Q2, 32)]
    Output: tuple of 2 tuple, use to load in matplotlib
    (Q1, Q2), (24, 32)
    """

    """
    Add period, group not apprear
    For example we want to see all month static but some month have no value => set sum aggeration to 0
    """
    if expect_labels:
        look_up = dict(rs)
        period = []
        aggregation = []
        for v in expect_labels:
            period.append(v)
            DEFAULT_AGGREGATION = 0
            aggregation.append(look_up.get(v, DEFAULT_AGGREGATION))
        return period , aggregation


    else:
        period, aggregation = zip(*rs)
        return period, aggregation
