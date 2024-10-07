from PyQt5 import QtWidgets, QtCore


class ReservationScene(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("Reservation Scene")
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)