from email.header import Header

from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView

from database.repositories.base_repository import Repository
from ui.scene.booking.booking_controller import BookingController
from ui.ui_booking_scene import Ui_ReservationScene
from qt_material import apply_stylesheet

class BookingScene(QtWidgets.QMainWindow):
    def __init__(self):
        self.controller = BookingController()
        super().__init__()
        self.ui = Ui_ReservationScene()
        self.ui.setupUi(self)
        self.ui.model = None
        self.setCentralWidget(self.ui.containerQwidget)
        self.init_ui()
        self.init_state()
        apply_stylesheet(self, theme='light_blue.xml')

    def init_ui(self):
        self.ui.model = QStandardItemModel()
        self.ui.model.setHorizontalHeaderLabels(['Guest ID', 'Room', 'Prime', "Checkin", "Status", "Action"])
        self.ui.booking_data_table.setStyleSheet("""
        border: none;
        background-color: white;  /* Màu nền */
        color: black;  /* Màu chữ */,
        """)
        self.ui.booking_data_table.setModel(self.ui.model)
        header = self.ui.booking_data_table.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { border: none; border-bottom: 2px solid black;  background-color: #FFFFFF }")
        header.setSectionResizeMode(QHeaderView.Stretch)
        # self.ui.model.beginInsertRows()
    
    def init_state(self):
        bookings = list(self.controller.get_all_bookings())
        for row, booking in enumerate(bookings):
            self.ui.model.setItem(row, 0, QStandardItem(str(booking.customer_id)))     # Customer ID
            self.ui.model.setItem(row, 1, QStandardItem(str(booking.room_id)))     # Customer ID
            self.ui.model.setItem(row, 2, QStandardItem(str(booking.room.price)))      # Start Date
            self.ui.model.setItem(row, 3, QStandardItem(str(booking.start_date)))        # End Date
            self.ui.model.setItem(row, 4, QStandardItem(str("Handling")))
            self.ui.model.setItem(row, 5, QStandardItem(str("Handling")))
