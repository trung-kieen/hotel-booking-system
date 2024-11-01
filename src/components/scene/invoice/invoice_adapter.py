"""
Author: Dang Xuan Lam
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem

from components.adapter.adapter import AdapterBase
from database.models.invoice import Invoice
from components.scene.booking.constant.booking_status import BookingStatus


class InvoiceAdapter(AdapterBase[Invoice]):

    def get_headers(self):
        return ["Invoice ID", "Customer Phone", "Customer Name", "Booking Status", "Total", "Pay Status",
                "Completed Date"]

    def add_item_to_model(self, row, invoice: Invoice):
        # Invoice ID
        item = QStandardItem(str(invoice.id))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        item.setData(invoice, Qt.UserRole)
        self.model.setItem(row, 0, item)

        # Customer phone
        item = QStandardItem(str(invoice.booking.customer.phone))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 1, item)

        # Customer Name
        item = QStandardItem(str(invoice.booking.customer.lastname + " " + invoice.booking.customer.firstname))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 2, item)

        # Booking Status
        item = QStandardItem(BookingStatus.get_status(invoice.booking).value)
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 3, item)

        # Total
        item = QStandardItem(str(round(invoice.total_price, 2)))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 4, item)

        # Pay Status
        item = QStandardItem(str(invoice.status.value))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 5, item)

        # Date
        item = QStandardItem(str(invoice.completed_at))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 6, item)
