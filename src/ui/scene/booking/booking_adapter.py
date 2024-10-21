from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from database.models.booking import Booking
from ui.scene.booking.constant.booking_status import BookingStatus


class BookingAdapter:
    def __init__(self, bookings=None):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['Guest Name', 'Room', "Start", "End", "Checkin", "Checkout", "Status"]
        )

    def set_items(self, bookings):
        """Cập nhật toàn bộ danh sách bookings và load vào model."""
        self.model.setRowCount(0)  # Xóa dữ liệu cũ trong model
        for row, booking in enumerate(bookings):
            self._add_booking_to_model(row, booking)

    def add_item(self, booking):
        """Thêm một booking vào model."""
        row = self.model.rowCount()
        self._add_booking_to_model(row, booking)

    def get_item(self, row) -> Booking | None:
        """Lấy một booking từ hàng tương ứng."""
        item = self.model.item(row, 0)  # Lấy item tại cột đầu tiên
        return item.data(Qt.UserRole)  # Lấy đối tượng Booking từ UserRole

    def _add_booking_to_model(self, row, booking):
        """Thêm một mục vào model tại hàng chỉ định và lưu đối tượng Booking."""
        # Guest Name
        item = QStandardItem(str(booking.customer.lastname + " " + booking.customer.firstname))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        item.setData(booking, Qt.UserRole)  # Lưu đối tượng Booking vào UserRole
        self.model.setItem(row, 0, item)

        # Room
        item = QStandardItem(str(booking.room_id // 10) + " - " + str(booking.room.floor_id))
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

    def get_model(self):
        """Trả về model để đổ vào QTableView."""
        return self.model

    def update_item(self, row, booking):
        """Cập nhật một booking tại hàng chỉ định."""
        # Cập nhật booking trong model
        self._add_booking_to_model(row, booking)
