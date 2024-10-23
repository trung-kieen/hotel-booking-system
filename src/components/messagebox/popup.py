"""
Author: Nguyen Khac Trung Kien
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox


from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

class BasePopup(QMessageBox):
    """Base popup object to display information.

    Args:
        title (str): Text to show on the title bar.
        message (str): Text to show in the main area.
        buttons (QMessageBox.StandardButtons, optional): Buttons to show below the popup. Defaults to the Ok button.
        icon (QMessageBox.Icon, optional): Icon to display on the popup. Defaults to NoIcon.
    """

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
    """Popup to display error messages.

    Args:
        title (str, optional): Text to show on the title bar. Defaults to "Error".
        message (str, optional): Text to show in the main area. Defaults to an empty string.
        buttons (QMessageBox.StandardButtons, optional): Buttons to show below the popup. Defaults to the Ok button.
    """

    def __init__(
        self,
        title: str = "Error",
        message: str = "",
        buttons: QMessageBox.StandardButtons = QMessageBox.Ok,
        *args,
        **kwargs
    ):
        super().__init__(title, message, buttons, QMessageBox.Critical, *args, **kwargs)
