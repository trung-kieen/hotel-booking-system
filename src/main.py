import sys
from database import fake_data

from components.app import App

# ============ Entity table must import here ==============
from database.engine import EngineHolder

# from database.models.user import User

# ========================================================

from database.orm import bootstrap
# from database.models.user import User


def main():

    engine = EngineHolder().get_engine()

    # Require to import all class inheritance with Base class (declarative_base)
    # If not explicit engine will not create table for those class
    bootstrap(engine)
    fake_data.fake()

    app = App(sys.argv)
    app.run()




if __name__ == "__main__":
    main()
