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
from database.models import *

# ========================================================

from database.orm import Session, bootstrap
# from database.models.user import User
from utils.constants import APP_NAME
from utils.settings import DATABASE_SQLITE_FILE





def main():

    engine = create_engine(f"sqlite:///{DATABASE_SQLITE_FILE}", echo=True)
    # Require to import all class inheritance with Base class (declarative_base)
    # If not explicit engine will not create table for those class
    bootstrap(engine)

    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)

    window = MainWindow()
    window.setGeometry(10, 100, 200, 500)

    window.maximumSize()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
