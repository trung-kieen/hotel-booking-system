"""
Author: Nguyen Khac Trung Kien
"""
from enum import Enum

from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget

class Color(Enum):
    SURFACE_BACKGROUND =  QColor(248, 250, 252)
    BASE_BACKGROUND = QColor(255 ,255 , 255)
    BUTTON_BACKGROUND = QColor( 100, 200, 255)
    PRIMARY_TEXT  = QColor(0, 0, 0)

class STYLE(Enum):
    PRIMARY_CONTAINER  = (Color.BASE_BACKGROUND.value , Color.PRIMARY_TEXT.value)
    SECONDARY_CONTAINER = (Color.SURFACE_BACKGROUND.value , Color.PRIMARY_TEXT. value)
    BUTTON= (Color.SURFACE_BACKGROUND.value , Color.PRIMARY_TEXT. value)


def set_style(widget: QWidget  , style  ):
    background , color = style
    set_widget_property(widget,background = background , text_color = color)


def set_widget_property(widget: QWidget, background  = None , text_color = None , reset_style : bool = True ):
    """

    """
    palette = widget.palette()
    if reset_style: widget.setStyleSheet("")
    if background: palette.setColor(QPalette.Window, background)
    if text_color: palette.setColor(QPalette.WindowText, text_color)
    widget.setPalette(palette)
    widget.setAutoFillBackground(True)
