"""
Author: Nguyen Khac Trung Kien
QT5 built-in method to load data to QTableView instead of mapping result set
"""
import logging

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
import math
from PyQt5.QtWidgets import QHeaderView, QTableView

from utils.settings import DATABASE_SQLITE_FILE
from utils.singleton import singleton

@singleton
class VTableConnectionHolder:
    def __init__(self) -> None:
        self.__db_engine = QSqlDatabase.addDatabase("QSQLITE")
        self.__db_engine.setDatabaseName(DATABASE_SQLITE_FILE)
        if self.__db_engine.open():
            logging.info('connect to SQL Server successfully')
        else:
            logging.error('connection failed')

    def get_db(self):
        return self.__db_engine
def excute_query (  sql_statement: str  , db: QSqlDatabase  =VTableConnectionHolder().get_db() ):
    """
    Return model result set to load into QViewTale
    """
    logging.info('processing query...')
    query_result = QSqlQuery(db)
    query_result.prepare(sql_statement)
    query_result.exec()
    return query_result


def fill_data( sql_statement: str ,view: QTableView):
    """
    Use to fill data from model result set to QTableView with table header from query column projection itself
    """
    model = QSqlQueryModel()
    query_result = excute_query(sql_statement)
    model.setQuery(query_result)
    view.setModel(model)
    return model

def adjust_size(view : QTableView):
    header = view.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.Stretch)
    view.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
