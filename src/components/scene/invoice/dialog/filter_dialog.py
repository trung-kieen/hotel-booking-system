"""
Author: Dang Xuan Lam
"""
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
                             QComboBox, QCheckBox, QDateEdit, QPushButton, QFormLayout)
from PyQt5.QtCore import QDate, Qt

from database.models.invoice import PaymentStatus
from components.scene.booking.constant.booking_status import BookingStatus


class InvoiceFilterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Invoice Filter")

        # Create a form layout for the filter fields
        form_layout = QFormLayout()

        # Customer Phone filter
        self.customer_phone_input = QLineEdit()
        form_layout.addRow(QLabel("Customer Phone:"), self.customer_phone_input)

        # Booking Status filter
        self.booking_status_input = QComboBox()
        self.booking_status_input.addItems(
            ["All"] + [v.value for v in BookingStatus.__members__.values()])
        form_layout.addRow(QLabel("Booking Status:"), self.booking_status_input)

        # Payment Status filter
        self.pay_status_input = QComboBox()
        self.pay_status_input.addItems(["All"] + [v.value for v in PaymentStatus.__members__.values()])
        form_layout.addRow(QLabel("Payment Status:"), self.pay_status_input)

        # Checkbox to enable/disable Completed Date filter
        self.completed_date_checkbox = QCheckBox("Enable Date Filter")
        self.completed_date_checkbox.stateChanged.connect(self.toggle_date_filter)

        # Completed Date
        self.completed_date_input = QDateEdit()
        self.completed_date_input.setCalendarPopup(True)  # Use a calendar popup for date input
        self.completed_date_input.setDate(QDate.currentDate())
        self.completed_date_input.setEnabled(False)  # Disable the date input initially

        # Add the checkbox and date input to the form
        form_layout.addRow(self.completed_date_checkbox)
        form_layout.addRow(QLabel("Completed Date:"), self.completed_date_input)

        # Apply and Cancel buttons
        button_layout = QHBoxLayout()
        apply_button = QPushButton("Apply Filter")
        apply_button.clicked.connect(self.accept)  # Trigger filtering when clicked
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(apply_button)
        button_layout.addWidget(cancel_button)

        # Set main layout
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def toggle_date_filter(self, state):
        """Enable or disable the Completed Date input based on the checkbox state."""
        if state == Qt.Checked:
            self.completed_date_input.setEnabled(True)
        else:
            self.completed_date_input.setEnabled(False)

    def get_filter_values(self):
        """Retrieve the values of the filter fields."""
        customer_phone = self.customer_phone_input.text()
        booking_status = self.booking_status_input.currentText()
        pay_status = self.pay_status_input.currentText()

        # Get date value only if the checkbox is checked
        if self.completed_date_checkbox.isChecked():
            completed_date = self.completed_date_input.date().toPyDate()
        else:
            completed_date = None

        return customer_phone, booking_status, pay_status, completed_date
