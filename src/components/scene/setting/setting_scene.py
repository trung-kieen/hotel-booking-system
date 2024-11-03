"""
Author: Dang Xuan Lam
"""
from PyQt5 import QtWidgets, QtCore


class SettingScene(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("Setting Scene")
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)
