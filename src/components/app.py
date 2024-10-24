from utils.constants import APP_NAME
import sys
from components.app_window import AppWindow
from PyQt5.QtWidgets import QApplication


class App(QApplication):
    maxHeight = 0
    maxWidth = 0

    def __init__(self, *argv) -> None:
        super().__init__(*argv)
        self.setApplicationName(APP_NAME)

        self.window = AppWindow()
        screen_geometry = self.primaryScreen().availableGeometry()
        App.maxWidth = screen_geometry.width()  # get max width
        App.maxHeight = screen_geometry.height()  # get max height
        self.window.setGeometry(screen_geometry)

    def run(self):
        self.window.show()
        sys.exit(self.exec_())
