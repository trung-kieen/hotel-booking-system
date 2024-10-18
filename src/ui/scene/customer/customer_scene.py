from PyQt5 import QtWidgets, QtCore
from database.models.customer import Customer
from database.engine import EngineHolder
from database.orm import  bootstrap

import sys
from fake_data import fake_data
from PyQt5.QtCore import QAbstractEventDispatcher, QSettings
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QTableWidgetItem
from sqlalchemy import Column, ForeignKey, Integer, String, except_, text
from sqlalchemy import create_engine
from sqlalchemy.orm import Relationship, base, declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# from ui.ui_customer_scene import Ui_CustomerScene
from utils.constants import APP_NAME
from utils.settings import DATABASE_SQLITE_FILE

# TODO
from ui.ui_customers_scene import Ui_MainWindow
from ui.ui_customer_dialog import Ui_Dialog as UICustomerDialog

should_insert = True


class AddCustomerDialog(QtWidgets.QDialog, UICustomerDialog ):
    def __init__(self, parent, session):
        super().__init__(parent)
        self.setupUi(self)  # Set up the UI from the generated class

        self.session = session
        self.birth.setDate(QtCore.QDate.currentDate().addDays(-2))
        self.buttonBox.accepted.connect(self.add_customer) # type: ignore

    def add_customer(self):
        # Get the values from the input fields
        # headers = ["ID", "First Name", "Last Name", "Address", "Birth", "Gender", "Phone", "Email"]
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

        self.session.add(new_customer)
        self.session.commit()

        self.accept()

class UpdateCustomerDialog(QtWidgets.QDialog, UICustomerDialog):
    def __init__(self, parent, customer_id, session):
        super().__init__(parent)
        self.setupUi(self)  # Set up the UI from the generated class

        self.session = session
        self.customer_id = customer_id
        self.customer = self.session.query(Customer).filter_by(id=self.customer_id).first()

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

        self.session.commit()

        self.accept()


class window(QtWidgets.QMainWindow):
    def __init__(self, engine = EngineHolder().get_engine()):
        super(window, self).__init__()
        self.engine = engine
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.container)
        self.load_customers()

        # register event
        self.ui.remove_customer_btn.clicked.connect(self.delete_customer)  # Connect delete button
        self.ui.edit_customer_btn.clicked.connect(self.open_edit_customer_dialog)  # Connect edit button
        self.ui.add_customer_btn.clicked.connect(self.open_add_customer_dialog)
        self.ui.exit_btn.clicked.connect(self.close)

    def open_add_customer_dialog(self):
        dialog = AddCustomerDialog(self, self.session)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            # Dialog was accepted, you can refresh your customer list or perform other actions
            print("Customer added successfully.")
            self.populate_table()
        else:
            print("Customer is not added!")

    def open_edit_customer_dialog(self):
        selected_row = self.ui.list_customers.currentRow()  # Get the selected row
        customer_id = int(self.ui.list_customers.item(selected_row, 0).text())
        dialog = UpdateCustomerDialog(self, customer_id, self.session)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            # Dialog was accepted, you can refresh your customer list or perform other actions
            print("Customer updated successfully.")
            self.populate_table()
        else:
            print("Customer is not updated!")

    def load_customers(self):
        headers = ["ID", "First Name", "Last Name", "Address", "Birth", "Gender", "Phone", "Email"]
        self.ui.list_customers.setColumnCount(len(headers))
        self.ui.list_customers.setHorizontalHeaderLabels(headers)

        self.populate_table()

    def edit_customer(self):
        pass

    def delete_customer(self):
        selected_row = self.ui.list_customers.currentRow()  # Get the selected row
        if selected_row < 0:
            QtWidgets.QMessageBox.warning(self, "Delete Customer", "Please select a customer to delete.")
            return

        # Get the customer ID from the selected row (assuming ID is in the first column)
        customer_id = int(self.ui.list_customers.item(selected_row, 0).text())

        # Confirm deletion
        reply = QtWidgets.QMessageBox.question(self, 'Confirm Delete',
                                                f"Are you sure you want to delete customer ID {customer_id}?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            # Delete the customer from the database
            self.session.query(Customer).filter(Customer.id == customer_id).delete()
            self.session.commit()

            # Refresh the table
            self.populate_table()
            QtWidgets.QMessageBox.information(self, "Delete Customer", "Customer deleted successfully.")



    def populate_table(self):
        # load customers from db
        customers = self.session.query(Customer).all()

        # Set the number of rows in the table based on the number of customers
        self.ui.list_customers.setRowCount(len(customers))

        # Insert each customer into the table
        for row, customer in enumerate(customers):
            self.ui.list_customers.setItem(row, 0, QTableWidgetItem(str(customer.id)))
            self.ui.list_customers.setItem(row, 1, QTableWidgetItem(customer.firstname))
            self.ui.list_customers.setItem(row, 2, QTableWidgetItem(customer.lastname))
            self.ui.list_customers.setItem(row, 3, QTableWidgetItem(customer.address))
            self.ui.list_customers.setItem(row, 4, QTableWidgetItem(str(customer.birth)))
            self.ui.list_customers.setItem(row, 5, QTableWidgetItem(customer.gender.value))
            self.ui.list_customers.setItem(row, 6, QTableWidgetItem(customer.phone))
            self.ui.list_customers.setItem(row, 7, QTableWidgetItem(customer.email))
