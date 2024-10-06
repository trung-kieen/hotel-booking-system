from utils.constants import APP_NAME
import sys
from components.app_window import AppWindow
from PyQt5.QtWidgets import QApplication
class App(QApplication):
    def __init__(self, *argv) -> None:
        super().__init__(*argv)
        self.setApplicationName(APP_NAME)

        self.window = AppWindow()
        self.window.maximumSize()

    def run(self):
        self.window.show()
        sys.exit(self.exec_())
