"""
Author: Dang Xuan Lam
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem

from components.adapter.adapter import AdapterBase
from database.models.booking import Booking
from components.scene.booking.constant.booking_status import BookingStatus


class BookingAdapter(AdapterBase[Booking]):

    def get_headers(self):
        return ['Guest Name', 'Room', "Start", "End", "Checkin", "Checkout", "Status"]

    def add_item_to_model(self, row, booking: Booking):
        """Thêm một mục vào model tại hàng chỉ định và lưu đối tượng Booking."""
        # Guest Name
        item = QStandardItem(str(booking.customer.lastname + " " + booking.customer.firstname))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        item.setData(booking, Qt.UserRole)  # Lưu đối tượng Booking vào UserRole
        self.model.setItem(row, 0, item)

        # Room
        item = QStandardItem(f"#{booking.room_id} Floor {booking.room.floor_id}")
        item.setTextAlignment(Qt.AlignCenter)
        item.setEditable(False)
        self.model.setItem(row, 1, item)

        # Start Day
        item = QStandardItem(str(booking.start_date.date()))
        item.setTextAlignment(Qt.AlignCenter)
        item.setEditable(False)
        self.model.setItem(row, 2, item)

        # End day
        item = QStandardItem(str(booking.end_date.date()))
        item.setTextAlignment(Qt.AlignCenter)
        item.setEditable(False)
        self.model.setItem(row, 3, item)

        # Checkin
        item = QStandardItem(str(booking.checkin))
        item.setTextAlignment(Qt.AlignCenter)
        item.setEditable(False)
        self.model.setItem(row, 4, item)

        # Checkout
        item = QStandardItem(str(booking.checkout))
        item.setTextAlignment(Qt.AlignCenter)
        item.setEditable(False)
        self.model.setItem(row, 5, item)

        # Status
        item = QStandardItem(BookingStatus.get_status(booking).value)
        item.setTextAlignment(Qt.AlignCenter)
        item.setEditable(False)
        self.model.setItem(row, 6, item)
