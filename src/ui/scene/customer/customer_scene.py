from PyQt5 import QtWidgets, QtCore
from database.models.customer import Customer
from database.engine import EngineHolder
from database.orm import  bootstrap

import sys
import copy
from fake_data import fake_data
from PyQt5.QtCore import QAbstractEventDispatcher, QSettings, Qt, QPoint, QSize
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem, QPainter
from PyQt5.QtWidgets import QApplication, QPushButton, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QStyledItemDelegate, QComboBox, QMenu
from sqlalchemy import Column, ForeignKey, Integer, String, except_, text
from sqlalchemy import create_engine
from sqlalchemy.orm import Relationship, base, declarative_base

from ui.scene.customer.customer_controller import CustomerController

# from ui.ui_customer_scene import Ui_CustomerScene
from utils.constants import APP_NAME
from utils.settings import DATABASE_SQLITE_FILE

# TODO
from ui.ui_customer_scene import Ui_CustomerScene
from ui.ui_customer_dialog import Ui_CustomerDialog
from ui.ui_filter_customer_dialog import Ui_FilterCustomerDialog
from qt_material import apply_stylesheet
import datetime

should_insert = True


class AddCustomerDialog(QtWidgets.QDialog, Ui_CustomerDialog):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.setupUi(self)  # Set up the UI from the generated class
        self.setWindowTitle("Add New Customer")
        self.gender.setFixedWidth(120)

        self.controller = controller
        self.birth.setDate(QtCore.QDate.currentDate().addDays(-2))
        self.buttonBox.accepted.connect(self.add_customer) # type: ignore

    def add_customer(self):
        # Get the values from the input fields
        firstname = self.firstname.text()
        lastname = self.lastname.text()
        address = self.address.text()
        birth_qdate = self.birth.date()  # Get the QDate
        birth = datetime.date(birth_qdate.year(), birth_qdate.month(), birth_qdate.day())
        gender = self.gender.currentText().upper()
        phone = self.phone.text()
        email = self.email.text()

        new_customer = Customer(firstname=firstname, lastname=lastname, address=address, \
                                birth=birth, gender=gender, phone=phone, email=email)

        self.controller.add_customer(new_customer)

        self.accept()

class UpdateCustomerDialog(QtWidgets.QDialog, Ui_CustomerDialog):
    def __init__(self, parent, controller, customer_id):
        super().__init__(parent)
        self.setupUi(self)  # Set up the UI from the generated class

        self.setWindowTitle("Update Customer")
        self.gender.setFixedWidth(120)

        self.controller = controller
        self.customer_id = customer_id
        self.customer = self.controller.find_customer_by_id(self.customer_id)

        self.firstname.setText(self.customer.firstname)
        self.lastname.setText(self.customer.lastname)
        self.address.setText(self.customer.address)
        self.birth.setDate(self.customer.birth)
        self.gender.setCurrentText(str(self.customer.gender.value).lower().capitalize())
        self.phone.setText(self.customer.phone)
        self.email.setText(self.customer.email)

        self.buttonBox.accepted.connect(self.update_customer) # type: ignore

    def update_customer(self):
        # Get the values from the input fields
        firstname = self.firstname.text()
        lastname = self.lastname.text()
        address = self.address.text()
        birth_qdate = self.birth.date()  # Get the QDate
        birth = datetime.date(birth_qdate.year(), birth_qdate.month(), birth_qdate.day())
        gender = self.gender.currentText().upper()
        phone = self.phone.text()
        email = self.email.text()

        self.customer.firstname = firstname
        self.customer.lastname = lastname
        self.customer.address = address
        self.customer.birth = birth
        self.customer.gender = gender
        self.customer.phone = phone
        self.customer.email = email

        self.controller.update_customer(self.customer)

        self.accept()


class FilterCustomerDialog(QtWidgets.QDialog, Ui_FilterCustomerDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)  # Set up the UI from the generated class

        self.setWindowTitle("Filter Customer")

        self.gender.setFixedWidth(120)
        self.filtered_gender = "None"
        self.buttonBox.accepted.connect(self.filter_customer) # type: ignore

    def filter_customer(self):
        # Get the values from the input fields
        gender = self.gender.currentText().lower().capitalize()

        self.filtered_gender = gender

        self.accept()

    def get_filtered_customers(self, customers):
        print(f"Filter by gender {self.filtered_gender}")
        if self.filtered_gender == 'None':
            return customers
        else:
            filtered_customers = []
            for customer in customers:
                if str(customer.gender.value) == self.filtered_gender:
                    filtered_customers.append(customer)

            return filtered_customers


class CustomerScene(QtWidgets.QMainWindow):
    def __init__(self, engine = EngineHolder().get_engine()):
        super(CustomerScene, self).__init__()
        self.engine = engine

        self.controller = CustomerController()
        self.ui = Ui_CustomerScene()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.containerQwidget)

        self.filtered_customers = []
        self.customers = []
        self.ui.model = None
        self.initUi()
        self.load_all_customers()
        apply_stylesheet(self, theme='light_blue.xml')

        self.filter_dialog = FilterCustomerDialog(self)

        # add new customer event
        self.ui.add_customer_btn.clicked.connect(self.open_add_customer_dialog)
        self.ui.filter_btn.clicked.connect(self.open_filter_customer_dialog)
        self.ui.search_bar.textChanged.connect(self.perform_search)

    def initUi(self):
        self.ui.model = QStandardItemModel()
        self.ui.model.setHorizontalHeaderLabels(["Customer ID", "First Name", "Last Name",
                                                 "Address", "Birth", "Gender", "Phone", "Email",
                                                 "Action"])
        self.ui.customer_data_table.setStyleSheet("""
        border: none;
        background-color: white;  /* Màu nền */
        color: black;  /* Màu chữ */,
        """)
        self.ui.customer_data_table.setModel(self.ui.model)
        header = self.ui.customer_data_table.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { border: none; border-bottom: 2px solid black;  background-color: #FFFFFF }")
        header.setSectionResizeMode(QHeaderView.Stretch)

    def open_filter_customer_dialog(self):
        if self.filter_dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.filtered_customers = self.filter_dialog.get_filtered_customers(self.customers)
            self.populate_table(self.filtered_customers)

    def open_add_customer_dialog(self):
        dialog = AddCustomerDialog(self, self.controller)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            QtWidgets.QMessageBox.information(self, "Add Customer", "Customer is added successfully.")
            self.load_all_customers()

    def open_edit_customer_dialog(self, customer_id):
        dialog = UpdateCustomerDialog(self, self.controller, customer_id)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            # Dialog was accepted, you can refresh your customer list or perform other actions
            QtWidgets.QMessageBox.information(self, "Update Customer", "Customer is updated successfully.")
            self.load_all_customers()

    def perform_search(self, text):
        if text == "":
            self.load_all_customers()
        else:
            self.customers = list(self.controller.search_customers_by_firstname_or_lastname(text))
            self.populate_table(self.customers)

    def load_all_customers(self):
        self.customers = list(self.controller.get_all_customers())
        self.populate_table(self.customers)

    def populate_table(self, customers):
        # load customers from db
        self.initUi()

        # Insert each customer into the table
        for row, customer in enumerate(customers):
            print(customer.id, " ", customer.firstname)
            self.ui.model.setItem(row, 0, QStandardItem(str(customer.id)))
            self.ui.model.setItem(row, 1, QStandardItem(str(customer.firstname)))
            self.ui.model.setItem(row, 2, QStandardItem(str(customer.lastname)))
            self.ui.model.setItem(row, 3, QStandardItem(str(customer.address)))
            self.ui.model.setItem(row, 4, QStandardItem(str(customer.birth)))
            self.ui.model.setItem(row, 5, QStandardItem(str(customer.gender.value)))
            self.ui.model.setItem(row, 6, QStandardItem(str(customer.phone)))
            self.ui.model.setItem(row, 7, QStandardItem(str(customer.email)))

            actionItem = QStandardItem()
            self.ui.model.setItem(row, 8, actionItem)

        for row, customer in enumerate(customers):
            combo_box = QComboBox()
            combo_box.addItems(["Action", "Edit", "Delete"])  # Add items to the combo box
            combo_box.activated.connect(lambda index, r=row, cb=combo_box: self.combo_action(index, r, cb))

            self.ui.customer_data_table.setIndexWidget(self.ui.model.index(row, 8), combo_box)


    def combo_action(self, index, row, combo_box):
        if index == 1:  # "Edit" selected
            self.handle_edit(row)
        elif index == 2:  # "Delete" selected
            self.handle_delete(row)

        combo_box.setCurrentIndex(0)  # Reset to "Select"

    def handle_edit(self, row):
        self.open_edit_customer_dialog(self.customers[row].id)

    def handle_delete(self, row):
        customer_id = self.customers[row].id
        reply = QtWidgets.QMessageBox.question(self, 'Confirm Delete',
                                                f"Are you sure you want to delete customer ID {customer_id}?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            # Delete the customer from the database
            self.controller.delete_customer(customer_id)
            self.load_all_customers()
            QtWidgets.QMessageBox.information(self, "Delete Customer", "Customer deleted successfully.")

