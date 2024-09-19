

from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Require entity class inheritance Base class to make table mapping to a table
Base = declarative_base()


Session = sessionmaker()


def bootstrap(engine):
    """
    Split module inspire by this topic
    https://stackoverflow.com/questions/51106264/how-do-i-split-an-sqlalchemy-declarative-model-into-modules
    """
    bind_engine(engine)
    create_metadata(engine)



def bind_engine(engine):
    Base.metadata.bind = engine
    Session.configure(bind=engine)
def create_metadata( engine):
    Base.metadata.create_all(engine)
