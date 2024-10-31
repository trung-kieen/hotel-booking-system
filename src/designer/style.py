"""
Author: Nguyen Khac Trung Kien
"""
from enum import Enum

from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QTableView, QWidget
from qt_material import apply_stylesheet
from sqlalchemy import table


class Color(Enum):
    SURFACE_BACKGROUND = QColor(248, 250, 252)
    BASE_BACKGROUND = QColor(255, 255, 255)
    BUTTON_BACKGROUND = QColor(100, 200, 255)
    PRIMARY_TEXT = QColor(0, 0, 0)


class STYLE(Enum):
    PRIMARY_CONTAINER = (Color.BASE_BACKGROUND.value, Color.PRIMARY_TEXT.value)
    SECONDARY_CONTAINER = (Color.SURFACE_BACKGROUND.value, Color.PRIMARY_TEXT.value)
    BUTTON = (Color.SURFACE_BACKGROUND.value, Color.PRIMARY_TEXT.value)
    MENU = """
            QMenu {
                background-color: #FFFFFF;
                color: #000000;
            }
            QMenu::item {
                background-color: transparent;
                color: #000000;
            }
            QMenu::item:selected {
                background-color: #87CEEB; /* Light Blue */
                color: #000000; /* Keep text color black */
            }
        """


def set_style(widget: QWidget, style):
    background, color = style
    set_widget_property(widget, background=background, text_color=color)


def set_widget_property(widget: QWidget, background=None, text_color=None, reset_style: bool = True):
    """

    """
    palette = widget.palette()
    if reset_style: widget.setStyleSheet("")
    if background: palette.setColor(QPalette.Window, background)
    if text_color: palette.setColor(QPalette.WindowText, text_color)
    widget.setPalette(palette)
    widget.setAutoFillBackground(True)


def set_style_button(widget: QWidget, style=None):
    widget.setStyleSheet("QPushButton {\n"
                         "                background-color: #007BFF;  /* Màu nền */\n"
                         "                color: white;                 /* Màu chữ */\n"
                         "                border: none;                 /* Không viền */\n"
                         "                border-radius: 10px;         /* Bo tròn góc */\n"
                         "                padding: 5px 10px;          /* Khoảng cách bên trong */\n"
                         "            }\n"
                         "            QPushButton:hover {\n"
                         "                background-color: #0056b3;   /* Màu nền khi di chuột qua */\n"
                         "            }")


def apply_theme(widget):
    apply_stylesheet(widget, theme='light_blue.xml', css_file='custom.css', extra={'font-size': '15px'})


def adjust_cmb(cmb):
    """
    Add space for combox when apply material theme `apply_theme(widget)`
    """
    border_offset = 25
    cmb.setFixedWidth(cmb.minimumSizeHint().width() + border_offset)


def adjust_view_table(tableWidget: QTableView):

    tableWidget.setSelectionMode(QtWidgets.QTableView.SingleSelection)
    tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
    header = tableWidget.horizontalHeader()
    header.setStyleSheet(
            "QHeaderView::section { border: none; border-bottom: 2px solid black;  background-color: #FFFFFF }"
    )
