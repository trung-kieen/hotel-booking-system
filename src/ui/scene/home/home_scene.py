from PyQt5 import QtWidgets, QtCore

from ui.ui_home_scene import Ui_HomeScene


class HomeScene(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomeScene()
        self.ui.setupUi(self)
        # layout = QtWidgets.QVBoxLayout(self)
        # label = QtWidgets.QLabel("Home Scene")
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # layout.addWidget(label)
