from PyQt5 import QtWidgets, QtCore


class CustomerScene(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("Guest Scene")
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)