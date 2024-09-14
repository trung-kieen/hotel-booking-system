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
from database.orm import Session, bootstrap
from database.user import User
from utils.constants import APP_NAME





def main():

    engine = create_engine("sqlite:///database.db", echo=True)
    # Require to import all class inheritance with Base class (declarative_base)
    # If not explicit engine will not create table for those class
    bootstrap(engine)

    print( "=" * 30)
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text(
                    "SELECT * FROM users"
                ),
            )
            results = result.fetchall()
            print(f"Selected rows: {results}")
    except Exception as e:
        print(f"Unexpected error while fetching records: {e}")
    print( "=" * 30)


    try:
        session= Session();
        user = User(id = 1 , firstname = "KIEN", lastname = "KAI", email = "AS")
        session.add(user)
        session.commit()
        session.close()
    except :
        print("ERROR")







    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)

    window = MainWindow()
    window.setGeometry(10, 100, 200, 500)

    window.maximumSize()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
