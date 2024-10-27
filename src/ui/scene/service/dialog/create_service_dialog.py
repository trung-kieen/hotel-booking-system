from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QHBoxLayout
from PyQt5.QtCore import Qt

from database.models.service import Service
from services.service_service import ServiceService


class CreateServiceDialog(QDialog):
    def __init__(self, parent=None):
        super(CreateServiceDialog, self).__init__(parent)
        self.setWindowTitle("Create New Service")

        # Tạo các thành phần giao diện
        self.name_input = QLineEdit(self)
        self.price_input = QLineEdit(self)
        self.save_button = QPushButton("Save", self)
        self.cancel_button = QPushButton("Cancel", self)

        # Định dạng giao diện
        self.layout = QVBoxLayout(self)

        form_layout = QFormLayout()
        form_layout.addRow(QLabel("Service Name:"), self.name_input)
        form_layout.addRow(QLabel("Price:"), self.price_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)

        self.layout.addLayout(form_layout)
        self.layout.addLayout(button_layout)

        # Kết nối nút với hành động
        self.save_button.clicked.connect(self.on_save)
        self.cancel_button.clicked.connect(self.reject)

    def on_save(self):
        """Xử lý khi nhấn nút Save."""
        name = self.name_input.text().strip()
        price = self.price_input.text().strip()

        if not name or not price:
            self.show_error("Both fields are required!")
            return

        try:
            price = float(price)
        except ValueError:
            self.show_error("Price must be a valid number!")
            return

        if price < 0:
            self.show_error("Price must be non-negative!")
            return

        ServiceService().create_service(Service(name=name, price=price))

        self.accept()  # Đóng dialog và trả về kết quả

    def show_error(self, message):
        """Hiển thị thông báo lỗi."""
        error_dialog = QDialog(self)
        error_dialog.setWindowTitle("Error")
        error_layout = QVBoxLayout(error_dialog)
        error_label = QLabel(message)
        error_label.setAlignment(Qt.AlignCenter)
        close_button = QPushButton("Close", error_dialog)
        close_button.clicked.connect(error_dialog.accept)

        error_layout.addWidget(error_label)
        error_layout.addWidget(close_button)
        error_dialog.exec_()
