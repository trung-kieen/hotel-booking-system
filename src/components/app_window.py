from PyQt5.QtWidgets import QApplication, QMainWindow
from designer.main_window import Ui_MainWindow
import sys


class AppWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.qwidgetContainer)

        # Stack window
        # TODO: Use constant for index value
        self.ui.customerButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.reservationButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.roomButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))



if __name__ == '__main__':
    app =  QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
