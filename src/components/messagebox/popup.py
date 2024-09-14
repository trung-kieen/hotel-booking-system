from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox


class BasePopup(QMessageBox):
    """Base popup object to display info

    Args:
        title (str): Text to show on the title bar
        message (str): Text to show on the main area
        buttons (StandardButtons, optional): Buttons to show below the popup.
        Defaults to Ok button
    """

    def __init__(
        self,
        title: str,
        message: str,
        buttons: QMessageBox.StandardButtons = QMessageBox.Ok,
        *args,
        **kwargs
    ):
        super().__init__(QMessageBox.NoIcon, title, message, buttons, *args, **kwargs)
        self.setAttribute(Qt.WA_DeleteOnClose)
