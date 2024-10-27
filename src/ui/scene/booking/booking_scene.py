from datetime import datetime

from PyQt5.QtWidgets import QHeaderView, QMenu, QDialog

from components.messagebox.popup import BasePopup
from database.models.booking import Booking
from designer.style import STYLE
from services.booking_service import BookingService
from ui.scene.booking.booking_adapter import BookingAdapter
from qt_material import apply_stylesheet
from PyQt5 import QtWidgets
from PyQt5.QtCore import QModelIndex, Qt

from ui.scene.booking.constant.booking_status import BookingStatus
from ui.scene.booking.dialog.booking_detail_dialog import BookingDetailDialog
from ui.scene.booking.dialog.booking_dialog import BookingDialog
from ui.scene.booking.dialog.filter_dialog import FilterDialog
from ui.scene.booking.dialog.pay_dialog import PayDialog
from ui.ui_booking_scene import Ui_ReservationScene


class BookingScene(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.service = BookingService()
        self.ui = Ui_ReservationScene()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.containerQwidget)

        # Khởi tạo Adapter
        self.adapter = BookingAdapter()

        # Gọi các hàm khởi tạo UI và dữ liệu
        self.init_ui()
        self.init_state()

        # Apply theme
        apply_stylesheet(self.ui, theme='light_blue.xml', extra={'font_size': '15px'})

    def init_ui(self):
        # Đổ model từ Adapter vào QTableView
        self.ui.booking_data_table.setModel(self.adapter.get_model())
        header = self.ui.booking_data_table.horizontalHeader()
        header.setStyleSheet(
            "QHeaderView::section { border: none; border-bottom: 2px solid black;  background-color: #FFFFFF }"
        )
        header.setSectionResizeMode(QHeaderView.Stretch)

        # self.ui.booking_data_table.setColumnWidth(7, 100)
        # self.ui.booking_data_table.horizontalHeader().setSectionResizeMode(7,
        #                                                                    QtWidgets.QHeaderView.Fixed)  # Cố định cột này

        # Gán sự kiện click và button
        self.ui.add_booking_btn.clicked.connect(self.add_booking)

        # menu for right click
        self.ui.booking_data_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.booking_data_table.customContextMenuRequested.connect(self.show_context_menu)

        self.ui.refresh_btn.clicked.connect(self.refresh_data)
        self.ui.filter_btn.clicked.connect(self.filter_data)

    def init_state(self):
        # Lấy dữ liệu từ controller và cập nhật vào adapter
        bookings = list(self.service.get_all_bookings())
        self.adapter.set_items(bookings)

    def add_booking(self):
        b = BookingDialog()
        b.exec()
        if b.booking is not None:
            MessageBox = BasePopup("Booking Message", "Booking successfully")
            MessageBox.exec()
            self.refresh_data()

    def show_context_menu(self, pos):
        model_index: QModelIndex = self.ui.booking_data_table.indexAt(pos)

        if model_index.isValid():  # Kiểm tra nếu vị trí nhấp là hợp lệ
            menu = QMenu(self)  # Tạo một menu
            menu.setStyleSheet(STYLE.MENU.value)
            action_edit = menu.addAction("Edit")
            action_details = menu.addAction("View Details")
            item = self.adapter.get_item(model_index.row())
            if item is not None:
                s = BookingStatus.get_status(item)
                if s == BookingStatus.InActive or s == BookingStatus.Late:
                    action_checkout = menu.addAction("Checkout")
                    action_checkout.triggered.connect(self.checkout)
                elif s == BookingStatus.InComing:
                    action_checkin = menu.addAction("Checkin")
                    action_checkin.triggered.connect(self.checkin)
                if s == BookingStatus.InComing:
                    action_checkin = menu.addAction("Cancel")
                    action_checkin.triggered.connect(self.cancel)
        # Kết nối các hành động với các phương thức xử lý
        action_edit.triggered.connect(lambda: self.edit_item(model_index))
        action_details.triggered.connect(lambda: self.view_details(model_index.row()))

        # Hiển thị menu tại vị trí chuột
        menu.exec_(self.ui.booking_data_table.mapToGlobal(pos))

    def edit_item(self, index):
        item = self.adapter.get_item(index.row())
        print(item)

    def view_details(self, index):
        BookingDetailDialog(self.adapter.get_item(index)).exec()

    def checkout(self):
        row_index = self.ui.booking_data_table.selectionModel().currentIndex().row()
        item = self.adapter.get_item(row_index)
        item.checkout = datetime.now()
        self.service.update_booking(item)
        self.adapter.update_item(row_index, item)
        d = PayDialog(item)
        d.exec()
        result = d.get_checkout_result()
        while result is None:
            d.exec()
            result = d.get_checkout_result()
            if result is not None:
                MessageBox = BasePopup("Booking Message", "Payment successfully")
                MessageBox.exec()
                self.refresh_data()
            else:
                MessageBox = BasePopup("Booking Message", "You must payment before exit")
                MessageBox.exec()

    def checkin(self):
        row_index = self.ui.booking_data_table.selectionModel().currentIndex().row()
        item = self.adapter.get_item(row_index)
        if item is not None:
            s = BookingStatus.get_status(item)
            now = datetime.now()
            if s == BookingStatus.InComing or s == BookingStatus.Late:
                if item.start_date <= now:
                    item.checkin = now
                    self.service.update_booking(item)
                    self.adapter.update_item(row_index, item)  # Cập nhật item trong adapter
                else:
                    BasePopup(f"Booking Message", "Cannot check in before the start time.").exec()
            else:
                BasePopup(f"Booking Message", f"Cannot check in due to status: {s}.").exec()

    def refresh_data(self):
        self.init_state()

    def cancel(self):
        row_index = self.ui.booking_data_table.selectionModel().currentIndex().row()
        item = self.adapter.get_item(row_index)
        if item is not None:
            s = BookingStatus.get_status(item)
            if s == BookingStatus.InComing or s == BookingStatus.Late:
                item.is_canceled = True
                self.service.update_booking(item)
                self.adapter.update_item(row_index, item)

    def filter_data(self):
        f = FilterDialog()
        if f.exec() == QDialog.Accepted:
            filters = f.apply_filter()

            filtered_bookings = self.service.filter_bookings(
                booking_type=filters.get("booking_type"),
                start_date=filters.get("start_date"),
                end_date=filters.get("end_date"),
                checkin=filters.get("checkin"),
                checkout=filters.get("checkout"),
                status=filters.get("status"),
                room_id=filters.get("room_number"),
                phone=filters.get("phone_number")
            )

            self.adapter.set_items(filtered_bookings)
