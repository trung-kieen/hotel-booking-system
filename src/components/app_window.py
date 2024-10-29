"""
Author: Nguyen Khac Trung Kien
Use to customize component style
"""
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow
import sys
import math

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

        self._initUi()
        self._initEvent()
        self._setCenter()

        self.stackContext = []
        self.ui.stackedWidget.addWidget(CustomerScene())
        self.ui.stackedWidget.addWidget(RoomScene())
        self.ui.stackedWidget.addWidget(BookingScene())
        self.ui.stackedWidget.addWidget(ServiceScene())
        self.ui.stackedWidget.addWidget(InvoiceScene())
        self.ui.stackedWidget.addWidget(HomeScene())

    def _initUi(self):
        self.setCentralWidget(self.ui.qwidgetContainer)
        self.ui.stackedWidget.setCurrentIndex(0)
        # set_style(self, STYLE.PRIMARY_CONTAINER.value)
        # set_style(self.ui.stackedWidget, STYLE.SECONDARY_CONTAINER.value)
        # set_style(self.ui.qwidgetContainer, STYLE.PRIMARY_CONTAINER.value)

        # set_style(self.ui.leftNavQwidget, STYLE.SECONDARY_CONTAINER.value)
        # TODO: Fix ui for button

        # apply_stylesheet(self, theme='light_blue.xml', invert_secondary=True, css_file="custom.css")
        # set_style(self.ui.reservationButton, STYLE.BUTTON.value)
        # set_style(self.ui.customerButton, STYLE.BUTTON.value)
        # set_style(self.ui.roomButton, STYLE.BUTTON.value)

    def _setCenter(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(math.floor((screen.width() - size.width()) / 2), math.floor((screen.height() - size.height()) / 2))

    def _initEvent(self):
        self.ui.customerButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.roomButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.reservationButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.service_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.invoice_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.homeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
