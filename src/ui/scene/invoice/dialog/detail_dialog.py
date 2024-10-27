from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QHeaderView, QTableView

from database.models.booking import Booking, BookingType
from database.models.customer import Customer
from ui.scene.invoice.dialog.ui_detail_dialog import Ui_Detail_Invoice_Dialog
from ui.scene.service.service_adapter import ServiceAdapter
from utils.bill_caculator import BillCalculator
from utils.invoice_caculator import BookingPriceCalculator


class InvoiceDetailDialog(QDialog):
    def __init__(self, invoice, parent=None):
        super().__init__(parent)
        self.invoice = invoice
        self.setWindowTitle("Invoice Detail")
        self.ui = Ui_Detail_Invoice_Dialog()
        self.ui.setupUi(self)
        self.init_personal_info(invoice.booking.customer)
        self.init_service_info(invoice.booking)
        self.init_bill_info(invoice.booking)

    def init_personal_info(self, customer: Customer):
        self.ui.phone_customer_lb.setText(customer.phone)
        self.ui.name_lb.setText(customer.lastname + " " + customer.firstname)

    def init_service_info(self, booking: Booking):
        data = [booking_service.service for booking_service in booking.booking_services]
        if len(data):
            adapter = ServiceAdapter()
            adapter.set_items(data)
            self.ui.service_data_table.setModel(adapter.get_model())
            header = self.ui.service_data_table.horizontalHeader()
            header.setStyleSheet(
                "QHeaderView::section { border: none; border-bottom: 2px solid black;  background-color: #FFFFFF }"
            )
            header.setSectionResizeMode(QHeaderView.Stretch)
            # Resize column and row to fit contents
            self.vertical_resize_table_view_to_contents(self.ui.service_data_table)
        else:
            self.ui.service_data_table.hide()

    def vertical_resize_table_view_to_contents(self, table_view: QTableView) -> None:
        row_total_height = 0

        # Tính chiều cao tổng của các hàng
        count = table_view.verticalHeader().count()
        for i in range(count):
            if not table_view.verticalHeader().isSectionHidden(i):
                row_total_height += table_view.verticalHeader().sectionSize(i)

        # Kiểm tra thanh cuộn ngang
        if not table_view.horizontalScrollBar().isHidden():
            row_total_height += table_view.horizontalScrollBar().height()

        # Kiểm tra tiêu đề ngang
        if not table_view.horizontalHeader().isHidden():
            row_total_height += table_view.horizontalHeader().height()

        # Đặt chiều cao tối thiểu cho QTableView
        table_view.setMinimumHeight(row_total_height)
        table_view.verticalHeader().hide()

    def init_bill_info(self, booking: Booking):
        bill_details = BillCalculator.calculate_bill_details(booking)

        # Set UI labels with the values from the calculation
        self.ui.room_price_lb.setText(bill_details['room_price_lb'])
        self.ui.duration_lb.setText(bill_details['duration_lb'])
        self.ui.service_total_price_lb.setText(bill_details['service_total_price_lb'])
        self.ui.room_total_price_lb.setText(bill_details['room_total_price_lb'])
        self.ui.total_price_lb.setText(bill_details['remaining_total_lb'])
        self.ui.prepaid_lb.setText(bill_details['prepaid_lb'])
        self.ui.ok_btn.clicked.connect(self.accept)
