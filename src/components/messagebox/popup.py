"""
Author: Nguyen Khac Trung Kien
Application popup menu
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox


from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from sqlalchemy.sql.operators import op

class BasePopup(QMessageBox):

    def __init__(
        self,
        title: str,
        message: str,
        buttons: QMessageBox.StandardButtons = QMessageBox.Ok,
        icon: QMessageBox.Icon = QMessageBox.NoIcon,
        *args,
        **kwargs
    ):
        super().__init__(icon, title, message, buttons, *args, **kwargs)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.exec_()


class ErrorPopup(BasePopup):

    def __init__(
        self,
        title: str = "Error",
        message: str = "",
        buttons: QMessageBox.StandardButtons = QMessageBox.Ok,
        *args,
        **kwargs
    ):
        super().__init__(title, message, buttons, QMessageBox.Critical, *args, **kwargs)

class CriticalPopup(BasePopup):

    def __init__(
        self,
        title: str = "Alert",
        message: str = "",
        buttons: QMessageBox.StandardButtons = QMessageBox.Ok,
        *args,
        **kwargs
    ):
        super().__init__(title, message, buttons, QMessageBox.Critical, *args, **kwargs)
