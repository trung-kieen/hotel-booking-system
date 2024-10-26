from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem

from components.adapter.adapter import AdapterBase
from database.models.invoice import Invoice


class InvoiceAdapter(AdapterBase[Invoice]):

    def get_headers(self):
        return ["Invoice ID", "Customer Phone", "Customer Name", "Total", "Date"]

    def add_item_to_model(self, row, item: Invoice):
        # Invoice ID
        item = QStandardItem(str(item.id))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        item.setData(item, Qt.UserRole)
        self.model.setItem(row, 0, item)

        # Customer phone
        item = QStandardItem(str(item.booking.customer.phone))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 1, item)

        # Customer Name
        item = QStandardItem(str(item.customer.lastname + " " + item.customer.firstname))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 2, item)

        # Total
        item = QStandardItem(str(item.total))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 3, item)

        # Date
        item = QStandardItem(str(item.date))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 4, item)
