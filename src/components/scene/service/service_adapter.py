from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem
from components.adapter.adapter import AdapterBase
from database.models.service import Service


class ServiceAdapter(AdapterBase[Service]):

    def get_headers(self):
        return ["Service ID", "Service Name", "Price", "Create At"]

    def add_item_to_model(self, row, data: Service):
        # Service ID
        item = QStandardItem(str(data.id))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        item.setData(data, Qt.UserRole)
        self.model.setItem(row, 0, item)

        # Service Name
        item = QStandardItem(str(data.name))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 1, item)

        # Price
        item = QStandardItem(str(round(data.price, 2)))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 2, item)

        # Description
        item = QStandardItem(str(data.created_at))
        item.setEditable(False)
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(row, 3, item)
