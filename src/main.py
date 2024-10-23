import sys
from fake_data import fake_data
from PyQt5.QtCore import QAbstractEventDispatcher, QSettings
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QTableWidgetItem
from sqlalchemy import Column, ForeignKey, Integer, String, except_, text
from sqlalchemy import create_engine
from sqlalchemy.orm import Relationship, base, declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


from components.app import App

# ============ Entity table must import here ==============
from database.engine import EngineHolder
from database.models import *
from database.models.customer import Customer

from database.orm import  bootstrap

# from database.models.user import User
from utils.logging import setup_logger_config
from utils.settings import DATABASE_SQLITE_FILE

# ========================================================

from database.orm import Session, bootstrap
# from database.models.user import User


def main():

    setup_logger_config()
    engine = EngineHolder().get_engine()

    # Require to import all class inheritance with Base class (declarative_base)
    # If not explicit engine will not create table for those class
    bootstrap(engine)
    fake_data.fake()

    app = App(sys.argv)
    app.run()




if __name__ == "__main__":
    main()
