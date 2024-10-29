"""
Author: Nguyen Khac Trung Kien
Use to customize component style
"""
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow
import sys
import math

from pipx.animate import animate

from ui.scene.customer.customer_scene import CustomerScene
from designer.style import STYLE
from designer.style import set_style
from ui.scene.booking.booking_scene import BookingScene
from ui.scene.invoice.invoice_scence import InvoiceScene
from ui.scene.room.room_scene import RoomScene
from ui.ui_main_window import Ui_MainWindow
from ui.scene.home.home_scene import HomeScene
from ui.scene.service.service_scene import ServiceScene


class AppWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.curr_btn = self.ui.homeButton
        self._initUi()
        self._initEvent()
        self._setCenter()
        self.stackContext = []
        self.ui.stackedWidget.addWidget(HomeScene())
        self.ui.stackedWidget.addWidget(CustomerScene())
        self.ui.stackedWidget.addWidget(RoomScene())
        self.ui.stackedWidget.addWidget(BookingScene())
        self.ui.stackedWidget.addWidget(ServiceScene())
        self.ui.stackedWidget.addWidget(InvoiceScene())

    def _initUi(self):
        self.setCentralWidget(self.ui.qwidgetContainer)
        self.changeScene(0, self.curr_btn)

    def _setCenter(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(math.floor((screen.width() - size.width()) / 2), math.floor((screen.height() - size.height()) / 2))

    def _initEvent(self):
        self.ui.homeButton.clicked.connect(lambda: self.changeScene(0, self.ui.homeButton))
        self.ui.customerButton.clicked.connect(lambda: self.changeScene(1, self.ui.customerButton))
        self.ui.roomButton.clicked.connect(lambda: self.changeScene(2, self.ui.roomButton))
        self.ui.reservationButton.clicked.connect(lambda: self.changeScene(3, self.ui.reservationButton))
        self.ui.service_btn.clicked.connect(lambda: self.changeScene(4, self.ui.service_btn))
        self.ui.invoice_btn.clicked.connect(lambda: self.changeScene(5, self.ui.invoice_btn))

    def changeScene(self, index, button):
        self.ui.stackedWidget.setCurrentIndex(index)
        self.animation(button)

    def animation(self, new_button):
        if self.curr_btn is not new_button:
            self.curr_btn.setStyleSheet("")
        if not new_button is None:
            new_button.setStyleSheet("background-color:  #007BFF ; color: white;")
            # Update the active button
            self.curr_btn = new_button


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
