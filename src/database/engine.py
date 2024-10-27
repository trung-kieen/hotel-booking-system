"""
Author: Nguyen Khac Trung Kien
"""
from collections.abc import Iterable, Sequence
from typing import Any
from sqlalchemy import Engine, Row, create_engine, text
from sqlalchemy.engine import connection_memoize
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


    def _execute(self, sql_stmt , *a  ,   **kw ):
        """
        Usage:
            # execute("...where id = :id", id=5)
        """
        with self._engine.begin() as conn:
            if kw:
                res = conn.execute(text(sql_stmt), kw)
            elif a:
                res = conn.execute(text(sql_stmt), a)
            else:
                res = conn.execute(text(sql_stmt), a)
            return res

    def all(self, sql_stmt , *   a  , **kw):
        """
        Usage: Iterable object
            for row in rs:
                print(row)
        """
        return self._execute(sql_stmt, *a, **kw).fetchall()


    def first(self, sql_stmt, *a: Any, **kw: Any) -> Any:
        """
        Usage: access by field name or position
            name = self.first(...)["name"]
        """
        return self._execute( sql_stmt, *a, **kw).first()
    def scalar(self, sql_stmt, *a: Any, **kw: Any) -> Any:
        return self._execute( sql_stmt, *a, **kw).scalar()



"""
@Deprecate event
TODO: Migrate constraint check
"""
# @event.listens_for(Engine, "connect")
# def set_sqlite_pragma(dbapi_connection, connection_record):
#     """
#     Read the docs! https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#sqlite-foreign-keys
#     """
#     cursor = dbapi_connection.cursor()
#     cursor.execute("PRAGMA foreign_keys=ON")
#     cursor.close()
