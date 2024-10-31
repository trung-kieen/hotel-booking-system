from abc import ABC, abstractmethod
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from typing_extensions import TypeVar

T = TypeVar('T')


class AdapterBase[T](ABC):
    def __init__(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(self.get_headers())

    @abstractmethod
    def get_headers(self):
        """Trả về danh sách tiêu đề cho mô hình."""
        pass

    def set_items(self, items: list[T]):
        """Cập nhật toàn bộ danh sách items vào mô hình."""
        self.model.setRowCount(0)  # Xóa dữ liệu cũ trong mô hình
        for row, item in enumerate(items):
            self.add_item_to_model(row, item)

    def add_item(self, item: T):
        """Thêm một item vào mô hình."""
        row = self.model.rowCount()
        self.add_item_to_model(row, item)

    def get_item(self, row) -> T:
        """Lấy một item từ hàng tương ứng."""
        return self.model.item(row, 0).data(Qt.UserRole)

    def update_item(self, row, item):
        """Cập nhật một item tại hàng chỉ định."""
        self.add_item_to_model(row, item)

    @abstractmethod
    def add_item_to_model(self, row, item: T):
        """Thêm item vào mô hình tại hàng chỉ định."""
        pass

    def get_model(self) -> QStandardItemModel:
        """Trả về mô hình để đổ vào QTableView."""
        return self.model
