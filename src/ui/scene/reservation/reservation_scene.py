from PyQt5 import QtWidgets, QtCore

from ui.ui_reservation_scene import Ui_ReservationScene


class ReservationScene( QtWidgets.QMainWindow ):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReservationScene()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.containerQwidget )
        # layout = QtWidgets.QVBoxLayout(self)
        # label = QtWidgets.QLabel("Reservation Scene")
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # layout.addWidget(label)
