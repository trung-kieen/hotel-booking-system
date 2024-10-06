import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QAbstractEventDispatcher, QSettings
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton
from sqlalchemy import Column, ForeignKey, Integer, String, except_, text
from sqlalchemy import create_engine
from sqlalchemy.orm import Relationship, base, declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from components.MainWindow import MainWindow


# ============ Entity table must import here ==============
from database.models.service import Service
from database.models.service_invoice import ServiceInvoice
from database.models.invoice import Invoice
from database.models.booking import Booking
from database.models.customer  import Customer
from database.models.room import Room
from database.models.bed_type import BedType
from database.models.bed_room import BedRoom

from database.models.floor import Floor
from database.models.review import Review
from database.models.hotel import Hotel
from database.orm import Base

# ========================================================

from database.orm import Session, bootstrap
# from database.models.user import User
from utils.constants import APP_NAME
from utils.settings import DATABASE_SQLITE_FILE



def insert_hotels(engine):
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # A list of hotels insert to db
    hotels = [
        Hotel(id=1, name="ABC", phone="09464646464"),
        Hotel(id=2, name="XYZ", phone="09464646464"),
        Hotel(id=3, name="123", phone="09434636412"),
        Hotel(id=4, name="456", phone="09434636413"),
    ]

    # Add the object to the session
    for hotel in hotels:
        session.merge(hotel)

    # Commit the transaction (inserts the row in the database)
    session.commit()

    # Close the session
    session.close()


def main():

    engine = create_engine(f"sqlite:///{DATABASE_SQLITE_FILE}", echo=True)

    # Require to import all class inheritance with Base class (declarative_base)
    # If not explicit engine will not create table for those class
    bootstrap(engine)

    # Insert hotels data
    insert_hotels(engine)

    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)

    window = MainWindow()
    window.setGeometry(10, 100, 200, 500)

    window.maximumSize()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
