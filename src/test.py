from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDesktopWidget, QTableView, QApplication
from qt_material import apply_stylesheet
import sys
import math
import logging

from utils.settings import DATABASE_SQLITE_FILE

SERVER_NAME = '<Server Name>'
DATABASE_NAME = '<Database Name>'
USERNAME = ''
PASSWORD = ''


STYLE_1 = """
QTableView{


    background-color: white;

    selection-background-color: black;

    border: none;



}

QHeaderView::section{

    border: none;

    height:20px;

    color: #1f1e21;

    font-size: 16px;

    font-weight: 600;

    font-family: Calibri;


    background-color: #dadde1;


    text-align: center;

    padding: 6px;
}



QTableView::item{

    background-color: white;

    border: none;

    background-color: rgb(220, 220, 220);

    selection-background-color: white;

    selection-color: black;

    font-family: Consolas;

    color: black;

    font-size: 11px;

    text-align: center;

    padding: 4px;

    margin: 3px;
}

QTableView::item:!alternate:!selected{

    background-color: white;

    selection-background-color: rgb(220, 220, 220);

    selection-color: black;

}

"""

def create_connection():
    # connString =f"sqlite:///{DATABASE_SQLITE_FILE}"
    global db
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("database.db")

    if db.open():
        logging.info('connect to SQL Server successfully')
        return True , db
    else:
        logging.error('connection failed')
        return False


def excute_query ( sql_statement):

    logging.info('processing query...')
    qry_result = QSqlQuery(db)
    qry_result.prepare(sql_statement)
    qry_result.exec()
    return qry_result

def displayData(sqlStatement):

    model = QSqlQueryModel()
    qry = excute_query(sqlStatement)
    model.setQuery(qry)

    view = QTableView()
    # view.setStyleSheet(STYLE_1)
    view.setModel(model)
    apply_stylesheet(view, theme='light_blue.xml', invert_secondary=True )
    screen = QDesktopWidget().screenGeometry()
    size = view.geometry()
    view.move(math.floor((screen.width() - size.width()) / 2), math.floor((screen.height() - size.height()) / 2))
    return view

if __name__=='__main__':
    app = QApplication(sys.argv)

    if create_connection():
        SQL_STATEMENT = 'SELECT * FROM customers LIMIT 10'
        dataView = displayData(SQL_STATEMENT)
        dataView.show()
    # apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True )
    app.exit()
    sys.exit(app.exec_())
