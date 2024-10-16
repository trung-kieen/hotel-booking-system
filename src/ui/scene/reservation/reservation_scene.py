from email.header import Header

from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QHeaderView

from ui.ui_reservation_scene import Ui_ReservationScene


class ReservationScene(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReservationScene()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.containerQwidget)
        self.init_ui()

    def init_ui(self):
        self.ui.model = QStandardItemModel()
        self.ui.model.setHorizontalHeaderLabels(['Guest ID', 'Room', 'Prime', "Checkin", "Status", "Action"])
        self.ui.booking_data_table.setStyleSheet("""
        border: none;
        background-color: white;  /* Màu nền */
        color: black;  /* Màu chữ */
        """)
        self.ui.booking_data_table.setModel(self.ui.model)
        header = self.ui.booking_data_table.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { border: none; border-bottom: 2px solid black;  background-color: #FFFFFF }")
        header.setSectionResizeMode(QHeaderView.Stretch)
        # self.ui.model.beginInsertRows()
