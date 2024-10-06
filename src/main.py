import sys

from sqlalchemy import  create_engine

from components.app import App

# ============ Entity table must import here ==============
from database.models import *
from database.orm import  bootstrap
from fake_data import fake_data

# from database.models.user import User
from utils.settings import DATABASE_SQLITE_FILE

# ========================================================


def main():
    engine = create_engine(f"sqlite:///{DATABASE_SQLITE_FILE}", echo=True)

    # Require to import all class inheritance with Base class (declarative_base)
    # If not explicit engine will not create table for those class
    bootstrap(engine)

    fake_data.fake(engine)
    app = App(sys.argv)
    app.run()



if __name__ == "__main__":
    main()
