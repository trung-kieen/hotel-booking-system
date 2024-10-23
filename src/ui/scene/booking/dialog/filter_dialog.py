from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, QCheckBox, \
    QHBoxLayout
from PyQt5.QtCore import QDate, Qt

from database.models.booking import BookingType
from ui.scene.booking.constant.booking_status import BookingStatus
from utils.singleton import singleton


@singleton
class FilterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Filter Bookings")
        from components.app import App
        self.resize(int(App.maxWidth * 1.5 / 4), int(App.maxHeight * 1.5 / 4))
        layout = QVBoxLayout()

        # Số điện thoại khách hàng
        self.phone_label = QLabel("Phone Number:")
        self.phone_input = QLineEdit()
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)

        # Room
        self.room_lb = QLabel("Room Number:")
        self.room_ip = QLineEdit()
        layout.addWidget(self.room_lb)
        layout.addWidget(self.room_ip)

        # Gom Start Date và End Date
        start_end_layout = QHBoxLayout()
        self.start_date_cb = QCheckBox("Filter by Start Date")
        self.start_date_input = QDateEdit()
        self.start_date_input.setCalendarPopup(True)
        self.start_date_input.setDate(QDate.currentDate())
        self.start_date_input.setEnabled(False)

        self.end_date_cb = QCheckBox("Filter by End Date")
        self.end_date_input = QDateEdit()
        self.end_date_input.setCalendarPopup(True)
        self.end_date_input.setDate(QDate.currentDate())
        self.end_date_input.setEnabled(False)

        l1 = QVBoxLayout()
        l2 = QVBoxLayout()
        l1.addWidget(self.start_date_cb)
        l1.addWidget(self.start_date_input)
        start_end_layout.addLayout(l1)
        l2.addWidget(self.end_date_cb)
        l2.addWidget(self.end_date_input)
        start_end_layout.addLayout(l2)
        layout.addLayout(start_end_layout)

        # Gom Checkin và Checkout
        checkin_checkout_layout = QHBoxLayout()
        self.checkin_cb = QCheckBox("Filter by Check-in Date")
        self.checkin_input = QDateEdit()
        self.checkin_input.setCalendarPopup(True)
        self.checkin_input.setDate(QDate.currentDate())
        self.checkin_input.setEnabled(False)

        self.checkout_cb = QCheckBox("Filter by Check-out Date")
        self.checkout_input = QDateEdit()
        self.checkout_input.setCalendarPopup(True)
        self.checkout_input.setDate(QDate.currentDate())
        self.checkout_input.setEnabled(False)

        l1 = QVBoxLayout()
        l2 = QVBoxLayout()
        l1.addWidget(self.checkin_cb)
        l1.addWidget(self.checkin_input)
        checkin_checkout_layout.addLayout(l1)
        l2.addWidget(self.checkout_cb)
        l2.addWidget(self.checkout_input)
        checkin_checkout_layout.addLayout(l2)
        layout.addLayout(checkin_checkout_layout)

        # Trạng thái booking
        self.status_label = QLabel("Status:")
        self.status_input = QComboBox()
        self.status_input.addItems(["All"] + [s.value for s in BookingStatus])
        layout.addWidget(self.status_label)
        layout.addWidget(self.status_input)

        # Loại booking (Hourly, Daily)
        self.booking_type_label = QLabel("Booking Type:")
        self.booking_type_input = QComboBox()
        self.booking_type_input.addItems(["All"] + [s.value for s in BookingType])
        layout.addWidget(self.booking_type_label)
        layout.addWidget(self.booking_type_input)

        # Nút áp dụng bộ lọc
        apply_button = QPushButton("Apply")
        apply_button.clicked.connect(self.apply_filter)
        layout.addWidget(apply_button)

        # Liên kết checkbox với việc bật/tắt ô nhập liệu
        self.start_date_cb.stateChanged.connect(lambda state: self.toggle_date_filter(self.start_date_input, state))
        self.end_date_cb.stateChanged.connect(lambda state: self.toggle_date_filter(self.end_date_input, state))
        self.checkin_cb.stateChanged.connect(lambda state: self.toggle_date_filter(self.checkin_input, state))
        self.checkout_cb.stateChanged.connect(lambda state: self.toggle_date_filter(self.checkout_input, state))

        self.setLayout(layout)

    def toggle_date_filter(self, date_input, state):
        """Bật/tắt trường ngày dựa vào checkbox."""
        date_input.setEnabled(state == Qt.Checked)

    def apply_filter(self):
        """Hàm này sẽ được gọi khi người dùng nhấn Apply."""
        filters = {}

        # Kiểm tra xem người dùng có nhập số phòng hay không
        room_number = (self.room_ip.text())
        if room_number:
            filters["room_number"] = room_number

        # Kiểm tra xem người dùng có nhập số điện thoại hay không
        phone_number = self.phone_input.text()
        if phone_number:
            filters["phone_number"] = phone_number

        # Lọc theo start date nếu checkbox được chọn
        if self.start_date_cb.isChecked():
            filters["start_date"] = self.start_date_input.date().toPyDate()

        # Lọc theo end date nếu checkbox được chọn
        if self.end_date_cb.isChecked():
            filters["end_date"] = self.end_date_input.date().toPyDate()

        # Lọc theo checkin date nếu checkbox được chọn
        if self.checkin_cb.isChecked():
            filters["checkin"] = self.checkin_input.date().toPyDate()

        # Lọc theo checkout date nếu checkbox được chọn
        if self.checkout_cb.isChecked():
            filters["checkout"] = self.checkout_input.date().toPyDate()

        # Kiểm tra xem người dùng có chọn trạng thái không
        status = self.status_input.currentText()
        if status != "None":
            filters["status"] = status

        # Kiểm tra loại booking (Hourly, Daily)
        booking_type = self.booking_type_input.currentText()
        if booking_type != "None":
            filters["booking_type"] = booking_type

        self.accept()
        return filters
