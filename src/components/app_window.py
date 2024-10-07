from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main.main_window import Ui_MainWindow
import sys

from ui.scene.customer.customer_scene import CustomerScene
from ui.scene.home.home_scene import HomeScene
from ui.scene.reservation.reservation_scene import ReservationScene
from ui.scene.room.room_scene import RoomScene
from ui.scene.service.service_scene import ServiceScene
from ui.scene.setting.setting_scene import SettingScene


class AppWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_scene([
            HomeScene(),
            CustomerScene(),
            ReservationScene(),
            RoomScene(),
            ServiceScene(),
            SettingScene()
        ])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
