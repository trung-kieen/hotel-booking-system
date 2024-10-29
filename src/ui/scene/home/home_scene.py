"""
Author: Nguyen Khac Trung Kien
"""
from typing import Optional, Union
import typing
from PyQt5 import QtWidgets, QtCore
from sqlalchemy import label

from utils import query as custom_query
from components.canvas import BookingCanvas, IncomeCanvas
from database.engine import EngineHolder
from services.home_service import HomeService
from ui.ui_home_scene import Ui_HomeScene
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget

class HomeScene( QtWidgets.QMainWindow ):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomeScene()
        self.ui.setupUi(self)
        self.service = HomeService()
        self.setCentralWidget(self.ui.containerQwidget )
        self.income_canvas = IncomeCanvas(self.ui.revenueChart)
        self.current_booking_canvas = BookingCanvas(self.ui.bookingChart)
        self.init_ui()
        self.register_event()
        self.load_statistic()
    def register_event(self):
        self.ui.rdMonth.toggled.connect(lambda: self.income_canvas.by_month())
        self.ui.rdQuarter.toggled.connect(lambda: self.income_canvas.by_quarter())
        self.ui.rdYear.toggled.connect(lambda: self.income_canvas.by_year())
        self.ui.rdMonth.setChecked(True)



    def load_statistic(self):
        today_income = self.service.today_revenue()
        total_customer = self.service.total_customers()
        total_reservation = self.service.total_booking()
        total_canceled_reservation = self.service.total_canceled_booking()
        total_success_reservation = self.service.total_success_booking()
        total_working_rooms = self.service.total_working_rooms()
        total_rooms = self.service.total_rooms()
        self.ui.lblTodayRevenue.setText(str(today_income))
        self.ui.lblTotalCustomer.setText(str(total_customer))
        self.ui.lblTotalReservation.setText(f"{total_success_reservation}/{total_canceled_reservation}/{total_reservation}")
        self.ui.lblAvailableRoom.setText(f"{total_working_rooms}/{total_rooms}")

    def init_ui(self):
        pass
