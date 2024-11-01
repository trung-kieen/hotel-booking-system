"""
Author: Nguyen Khac Trung Kien
Manager orm session
Bootstrap database from entity model
Handle circle import while bind engine
"""

from sqlalchemy import Engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import DropConstraint


# Require entity class inheritance Base class to make table mapping to a table
Base = declarative_base()


Session = sessionmaker()


def bootstrap(engine):
    """
    Split module inspire by this topic
    https://stackoverflow.com/questions/51106264/how-do-i-split-an-sqlalchemy-declarative-model-into-modules
    """
    bind_engine(engine)
    recreate_metadata(engine)



def bind_engine(engine):
    Base.metadata.bind = engine
    Session.configure(bind=engine)

def recreate_metadata( engine):
    """
    Override DDL change in database or create new one.
    @See sqlalchemy.MetaData
    """
    Base.metadata.drop_all(engine )
    Base.metadata.create_all(engine, checkfirst = True)
