# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/trungkieen/project/hotel-booking-system/src/ui/ui_service_scene.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SerivceScene(object):
    def setupUi(self, SerivceScene):
        SerivceScene.setObjectName("SerivceScene")
        SerivceScene.resize(802, 590)
        self.containerQwidget = QtWidgets.QWidget(SerivceScene)
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
        self.search_ld = QtWidgets.QLineEdit(self.widget_2)
        self.search_ld.setObjectName("search_ld")
        self.horizontalLayout_3.addWidget(self.search_ld)
        self.search_btn = QtWidgets.QPushButton(self.widget_2)
        self.search_btn.setStyleSheet("QPushButton {\n"
"                background-color: #007BFF;  /* Màu nền */\n"
"                color: white;                 /* Màu chữ */\n"
"                border: none;                 /* Không viền */\n"
"                border-radius: 10px;         /* Bo tròn góc */\n"
"                padding: 5px 10px;          /* Khoảng cách bên trong */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0056b3;   /* Màu nền khi di chuột qua */\n"
"            }")
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_3.addWidget(self.search_btn)
        self.create_new_service_btn = QtWidgets.QPushButton(self.widget_2)
        self.create_new_service_btn.setStyleSheet("QPushButton {\n"
"                background-color: #007BFF;  /* Màu nền */\n"
"                color: white;                 /* Màu chữ */\n"
"                border: none;                 /* Không viền */\n"
"                border-radius: 10px;         /* Bo tròn góc */\n"
"                padding: 5px 10px;          /* Khoảng cách bên trong */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0056b3;   /* Màu nền khi di chuột qua */\n"
"            }")
        self.create_new_service_btn.setFlat(True)
        self.create_new_service_btn.setObjectName("create_new_service_btn")
        self.horizontalLayout_3.addWidget(self.create_new_service_btn)
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
        self.service_data_table = QtWidgets.QTableView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.service_data_table.sizePolicy().hasHeightForWidth())
        self.service_data_table.setSizePolicy(sizePolicy)
        self.service_data_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.service_data_table.setShowGrid(False)
        self.service_data_table.setSortingEnabled(True)
        self.service_data_table.setObjectName("service_data_table")
        self.service_data_table.horizontalHeader().setCascadingSectionResizes(False)
        self.service_data_table.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_2.addWidget(self.service_data_table)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(0, 8)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(SerivceScene)
        QtCore.QMetaObject.connectSlotsByName(SerivceScene)

    def retranslateUi(self, SerivceScene):
        _translate = QtCore.QCoreApplication.translate
        SerivceScene.setWindowTitle(_translate("SerivceScene", "Hotel"))
        self.search_btn.setText(_translate("SerivceScene", "Search"))
        self.create_new_service_btn.setText(_translate("SerivceScene", "Create New Service"))
        self.refresh_btn.setText(_translate("SerivceScene", "↻"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SerivceScene = QtWidgets.QWidget()
    ui = Ui_SerivceScene()
    ui.setupUi(SerivceScene)
    SerivceScene.show()
    sys.exit(app.exec_())
