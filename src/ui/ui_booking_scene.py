# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dxlaam/Projects/hotel-booking-system/src/ui/ui_booking_scene.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReservationScene(object):
    def setupUi(self, ReservationScene):
        ReservationScene.setObjectName("ReservationScene")
        ReservationScene.resize(802, 590)
        self.containerQwidget = QtWidgets.QWidget(ReservationScene)
        self.containerQwidget.setGeometry(QtCore.QRect(-10, -10, 821, 611))
        self.containerQwidget.setStyleSheet("")
        self.containerQwidget.setObjectName("containerQwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.containerQwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.containerQwidget)
        self.widget.setStyleSheet("background-color: #FFFFFF")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.filter_btn = QtWidgets.QPushButton(self.widget_2)
        self.filter_btn.setStyleSheet("QPushButton {\n"
"                background-color: #007BFF;  /* Màu nền */\n"
"                color: white;                 /* Màu chữ */\n"
"                border: none;                 /* Không viền */\n"
"                border-radius: 10px;         /* Bo tròn góc */\n"
"                padding: 5px 10px;          /* Khoảng cách bên trong */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0056b3;   /* Màu nền khi di chuột qua */\n"
"            }")
        self.filter_btn.setObjectName("filter_btn")
        self.horizontalLayout_3.addWidget(self.filter_btn)
        self.add_booking_btn = QtWidgets.QPushButton(self.widget_2)
        self.add_booking_btn.setStyleSheet("QPushButton {\n"
"                background-color: #007BFF;  /* Màu nền */\n"
"                color: white;                 /* Màu chữ */\n"
"                border: none;                 /* Không viền */\n"
"                border-radius: 10px;         /* Bo tròn góc */\n"
"                padding: 5px 10px;          /* Khoảng cách bên trong */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0056b3;   /* Màu nền khi di chuột qua */\n"
"            }")
        self.add_booking_btn.setFlat(True)
        self.add_booking_btn.setObjectName("add_booking_btn")
        self.horizontalLayout_3.addWidget(self.add_booking_btn)
        self.refresh_btn = QtWidgets.QPushButton(self.widget_2)
        self.refresh_btn.setStyleSheet("QPushButton {\n"
"                background-color: #007BFF;  /* Màu nền */\n"
"                color: white;                 /* Màu chữ */\n"
"                border: none;                 /* Không viền */\n"
"                border-radius: 10px;         /* Bo tròn góc */\n"
"                padding: 5px 10px;          /* Khoảng cách bên trong */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0056b3;   /* Màu nền khi di chuột qua */\n"
"            }")
        self.refresh_btn.setFlat(True)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout_3.addWidget(self.refresh_btn)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.booking_data_table = QtWidgets.QTableView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.booking_data_table.sizePolicy().hasHeightForWidth())
        self.booking_data_table.setSizePolicy(sizePolicy)
        self.booking_data_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.booking_data_table.setShowGrid(False)
        self.booking_data_table.setSortingEnabled(True)
        self.booking_data_table.setObjectName("booking_data_table")
        self.booking_data_table.horizontalHeader().setCascadingSectionResizes(False)
        self.booking_data_table.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_2.addWidget(self.booking_data_table)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(0, 8)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(ReservationScene)
        QtCore.QMetaObject.connectSlotsByName(ReservationScene)

    def retranslateUi(self, ReservationScene):
        _translate = QtCore.QCoreApplication.translate
        ReservationScene.setWindowTitle(_translate("ReservationScene", "Hotel"))
        self.filter_btn.setText(_translate("ReservationScene", "Filter"))
        self.add_booking_btn.setText(_translate("ReservationScene", "Create New Booking"))
        self.refresh_btn.setText(_translate("ReservationScene", "↻"))
