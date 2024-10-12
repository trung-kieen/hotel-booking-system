"""
Author: Nguyen Khac Trung Kien
Use to customize component style
"""
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from designer.style import STYLE
from designer.style import  set_style
from ui.scene.customer.customer_scene import CustomerScene
from ui.scene.reservation.reservation_scene import ReservationScene
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

        # self.scene = [HomeScene(), ServiceScene()]
        # for w in self.scene:
        #     self.ui.stackedWidget.addWidget(w)


        buttons = []
        # buttons.append( (self.ui.roomButton , RoomScene() )
        # buttons.append( , (self.ui.reservationButton , ReservationScene() ) , self.ui.customerButton))
        self.stackContext = []
        self.ui.stackedWidget.addWidget( CustomerScene())
        self.ui.stackedWidget.addWidget( RoomScene())
        self.ui.stackedWidget.addWidget(ReservationScene())




    def _initUi(self):
        self.setCentralWidget(self.ui.qwidgetContainer)
        set_style(self, STYLE.PRIMARY_CONTAINER.value)
        set_style(self.ui.stackedWidget, STYLE.SECONDARY_CONTAINER.value)
        set_style(self.ui.qwidgetContainer, STYLE.PRIMARY_CONTAINER.value)

        set_style(self.ui.leftNavQwidget, STYLE.SECONDARY_CONTAINER.value)


        #TODO: Fix ui for button
        set_style(self.ui.reservationButton, STYLE.BUTTON.value)
        set_style(self.ui.customerButton, STYLE.BUTTON.value)
        set_style(self.ui.roomButton, STYLE.BUTTON.value)



    def _initEvent(self):
        self.ui.customerButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.roomButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.reservationButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
