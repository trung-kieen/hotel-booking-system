from PyQt5.QtWidgets import QDialog
from utils.singleton import singleton


@singleton
class FilterDialog(QDialog):

    def __init__(self, parent=None):
        super(FilterDialog, self).__init__(parent)
        # self.ui = Ui_Checkout_Dialog()
        self.ui.setupUi(self)
        from components.app import App
        self.resize(int(App.maxWidth * 3 / 4), int(App.maxHeight * 3 / 4))

    def get_filter_result(self):
        pass
