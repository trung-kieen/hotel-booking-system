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
        # rs = EngineHolder().all("SELECT COUNT(*) FROM bookings WHERE room_id = :room_id", room_id = 1)
        # print(type(rs))
        # print(rs)
        # layout = QtWidgets.QVBoxLayout(self)
        # label = QtWidgets.QLabel("Home Scene")
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # layout.addWidget(label)
        self.init_ui()
    def init_ui(self):

        # Add labels for each metric
        # self.ui.group_income.addwidget(qlabel("total working rooms:"), 0, 0)
        # self.ui.containerQwidget.addWidget(QLabel(str(self.service.total_working_rooms())), 0, 1)

        # container.addWidget(QLabel(), 1, 1)

        # container.addWidget(QLabel("Total Customers:"), 2, 0)
        # container.addWidget(QLabel(str(self.service.total_customers())), 2, 1)

        # container.addWidget(QLabel("Total Bookings:"), 3, 0)
        # container.addWidget(QLabel(str(self.service.total_booking())), 3, 1)

        # container.addWidget(QLabel("Successful Bookings:"), 4, 0)
        # container.addWidget(QLabel(str(self.service.total_success_booking())), 4, 1)

        # container.addWidget(QLabel("Canceled Bookings:"), 5, 0)
        # container.addWidget(QLabel(str(self.service.total_canceled_booking())), 5, 1)
        # # income = self.service.income_by_month()

        # # period , group_income= zip(*income)

        # StaticGrid(parent=self.ui.horizontalLayout, label_text = "HI",value ="123")

        income_canvas = IncomeCanvas(self.ui.revenueChart)
        current_booking_canvas = BookingCanvas(self.ui.bookingChart)






# if __name__ == '__main__':
#     HomeScene()
