"""
Author: Dang Xuan Lam
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QHeaderView

from database.models.booking import Booking
from components.scene.booking.constant.booking_status import BookingStatus
from components.scene.booking.dialog.ui.ui_booking_detail import Ui_Booking_Details_Dialog


class BookingDetailDialog(QDialog):
    def __init__(self, booking=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Booking Dialog")
        self.ui = Ui_Booking_Details_Dialog()
        self.ui.setupUi(self)
        from components.app import App
        self.resize(int(App.maxWidth * 3 / 4), 0)
        self.init_ui_personal_container(booking.customer)
        self.init_booking_container(booking)
        self.init_room_container(booking.room)

    def init_ui_personal_container(self, customer):
        self.ui.name_lb.setText(str(customer.lastname + ' ' + customer.firstname))
        self.ui.address_lb.setText(str(customer.address))
        self.ui.id_lb.setText(str(customer.uuid))
        self.ui.phone_number_lb.setText(str(customer.phone))

    def init_booking_container(self, booking: Booking):
        header = self.ui.booking_tb.horizontalHeader()
        header.setStyleSheet(
            "QHeaderView::section { border: none; border-bottom: 2px solid black;  background-color: #FFFFFF }"
        )
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.model = QStandardItemModel()
        self.ui.model.setHorizontalHeaderLabels([
            "Guest CCCD", "Number of Guest", "Start", "Checkin", "End", "Checkout", "Status"
        ])
        item = QStandardItem(str(booking.customer.uuid))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        item.setData(str(booking.customer.id), Qt.ToolTipRole)
        self.ui.model.setItem(0, 0, item)

        item = QStandardItem(str(booking.num_adults + booking.num_children))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.model.setItem(0, 1, item)

        item = QStandardItem(str(booking.start_date.date()))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.model.setItem(0, 2, item)

        item = QStandardItem(str(booking.checkin))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.model.setItem(0, 3, item)

        item = QStandardItem(str(booking.end_date.date()))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.model.setItem(0, 4, item)

        item = QStandardItem(str(booking.checkout))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.model.setItem(0, 5, item)

        item = QStandardItem(BookingStatus.get_status(booking).value)
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.model.setItem(0, 6, item)

        self.ui.booking_tb.setModel(self.ui.model)

        self.setMouseTracking(True)

    def init_room_container(self, room):
        header = self.ui.room_tb.horizontalHeader()
        header.setStyleSheet(
            "QHeaderView::section { border: none; border-bottom: 2px solid black;  background-color: #FFFFFF }"
        )
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.model = QStandardItemModel()
        self.ui.model.setHorizontalHeaderLabels([
            "Room ID", "Room Type", "Room Floor", "Price"
        ])
        item = QStandardItem(str(room.id))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.model.setItem(0, 0, item)

        item = QStandardItem(str(room.room_type))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.model.setItem(0, 1, item)

        item = QStandardItem(str(room.floor_id))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.model.setItem(0, 2, item)

        item = QStandardItem(str(room.price))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.model.setItem(0, 3, item)

        self.ui.room_tb.setModel(self.ui.model)
