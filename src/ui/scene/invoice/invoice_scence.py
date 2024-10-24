from PyQt5 import QtWidgets

from ui.ui_service_scene import Ui_SerivceScene


class InvoiceScene(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SerivceScene()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.containerQwidget)