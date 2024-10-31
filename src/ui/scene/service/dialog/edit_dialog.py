from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout
from database.models.service import Service


class EditServiceDialog(QDialog):
    def __init__(self, service: Service, parent=None):
        super(EditServiceDialog, self).__init__(parent)
        self.service = service
        self.setWindowTitle("Edit Service")

        # Create form layout for the service details
        layout = QFormLayout()

        # Service Name
        self.name_input = QLineEdit(self.service.name)
        layout.addRow("Service Name:", self.name_input)

        # Service Price
        self.price_input = QLineEdit(str(self.service.price))
        layout.addRow("Service Price:", self.price_input)

        # Buttons
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_changes)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_changes(self):
        self.service.name = self.name_input.text()
        self.service.price = float(self.price_input.text())

        # Save the updated service object to the database
        # Example: service_repository.update(self.service)

        # Close the dialog
        self.accept()
