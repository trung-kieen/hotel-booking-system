"""
Author: Nguyen Khac Trung Kien
"""
from sqlalchemy import Engine, create_engine
from sqlalchemy.engine.create import event

from database.orm import Session
from utils.settings import DATABASE_SQLITE_FILE
from utils.singleton import singleton
@singleton
class EngineHolder:
    def __init__(self) -> None:
        self._engine = create_engine(f"sqlite:///{DATABASE_SQLITE_FILE}", echo=True)

    def get_engine(self):
        return self._engine




# @event.listens_for(Engine, "connect")
# def set_sqlite_pragma(dbapi_connection, connection_record):
#     """
#     Read the docs! https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#sqlite-foreign-keys
#     """
#     cursor = dbapi_connection.cursor()
#     cursor.execute("PRAGMA foreign_keys=ON")
#     cursor.close()
