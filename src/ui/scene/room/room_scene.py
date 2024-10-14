from PyQt5 import QtWidgets, QtCore

from ui.ui_room_scene import Ui_RoomScene


class RoomScene( QtWidgets.QMainWindow ):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RoomScene()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.containerQwidget )
        # layout = QtWidgets.QVBoxLayout(self)
        # label = QtWidgets.QLabel("Room Scene")
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # layout.addWidget(label)
