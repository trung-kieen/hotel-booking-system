# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dxlaam/Projects/hotel-booking-system/src/ui/scene/invoice/dialog/ui_detail_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Detail_Invoice_Dialog(object):
    def setupUi(self, Detail_Invoice_Dialog):
        Detail_Invoice_Dialog.setObjectName("Detail_Invoice_Dialog")
        Detail_Invoice_Dialog.resize(950, 705)
        Detail_Invoice_Dialog.setStyleSheet("QPushButton {\n"
"          background-color: #007BFF;\n"
"              color: white;  \n"
"              border: none;                \n"
"              border-radius: 10px;        \n"
"             padding: 5px 10px;        \n"
"         }\n"
"          QPushButton:hover {\n"
"               background-color: #0056b3;   \n"
"           }\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(Detail_Invoice_Dialog)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.scrollArea = QtWidgets.QScrollArea(Detail_Invoice_Dialog)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 916, 755))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalWidget.setStyleSheet("QFrame#personal_information_container, QFrame#room_information_container,\n"
"QFrame#booking_summary_container, \n"
"QFrame#bill_container, \n"
"QFrame#room_filter_container,\n"
"QFrame#bill_container\n"
"{\n"
"                            border: 2px solid black;\n"
"                            border-radius: 15px;\n"
"                            }\n"
"                        ")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.personal_information_container = QtWidgets.QFrame(self.verticalWidget)
        self.personal_information_container.setStyleSheet("")
        self.personal_information_container.setFrameShape(QtWidgets.QFrame.Panel)
        self.personal_information_container.setFrameShadow(QtWidgets.QFrame.Plain)
        self.personal_information_container.setObjectName("personal_information_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.personal_information_container)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_lb = QtWidgets.QLabel(self.personal_information_container)
        self.label_lb.setObjectName("label_lb")
        self.verticalLayout_2.addWidget(self.label_lb)
        self.phone_container = QtWidgets.QWidget(self.personal_information_container)
        self.phone_container.setObjectName("phone_container")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.phone_container)
        self.horizontalLayout_3.setContentsMargins(15, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.phone_container)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.phone_customer_lb = QtWidgets.QLabel(self.phone_container)
        self.phone_customer_lb.setText("")
        self.phone_customer_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_customer_lb.setObjectName("phone_customer_lb")
        self.horizontalLayout_3.addWidget(self.phone_customer_lb)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 9)
        self.verticalLayout_2.addWidget(self.phone_container)
        self.name_container = QtWidgets.QWidget(self.personal_information_container)
        self.name_container.setObjectName("name_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.name_container)
        self.horizontalLayout_5.setContentsMargins(15, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.name_container)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.name_lb = QtWidgets.QLabel(self.name_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_lb.sizePolicy().hasHeightForWidth())
        self.name_lb.setSizePolicy(sizePolicy)
        self.name_lb.setText("")
        self.name_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lb.setObjectName("name_lb")
        self.horizontalLayout_5.addWidget(self.name_lb)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 9)
        self.verticalLayout_2.addWidget(self.name_container)
        self.message_personal_infor_lb = QtWidgets.QLabel(self.personal_information_container)
        self.message_personal_infor_lb.setStyleSheet("color: red;")
        self.message_personal_infor_lb.setText("")
        self.message_personal_infor_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.message_personal_infor_lb.setObjectName("message_personal_infor_lb")
        self.verticalLayout_2.addWidget(self.message_personal_infor_lb)
        self.verticalLayout.addWidget(self.personal_information_container)
        self.room_filter_container = QtWidgets.QFrame(self.verticalWidget)
        self.room_filter_container.setStyleSheet("")
        self.room_filter_container.setFrameShape(QtWidgets.QFrame.Panel)
        self.room_filter_container.setFrameShadow(QtWidgets.QFrame.Plain)
        self.room_filter_container.setObjectName("room_filter_container")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.room_filter_container)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalWidget_14 = QtWidgets.QWidget(self.room_filter_container)
        self.horizontalWidget_14.setObjectName("horizontalWidget_14")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.horizontalWidget_14)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.horizontalWidget_14)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.service_data_table = QtWidgets.QTableView(self.horizontalWidget_14)
        self.service_data_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.service_data_table.setObjectName("service_data_table")
        self.verticalLayout_5.addWidget(self.service_data_table)
        self.verticalLayout_25.addWidget(self.horizontalWidget_14)
        self.verticalLayout.addWidget(self.room_filter_container)
        self.bill_container = QtWidgets.QFrame(self.verticalWidget)
        self.bill_container.setStyleSheet("")
        self.bill_container.setFrameShape(QtWidgets.QFrame.Panel)
        self.bill_container.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bill_container.setObjectName("bill_container")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.bill_container)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalWidget_15 = QtWidgets.QWidget(self.bill_container)
        self.horizontalWidget_15.setObjectName("horizontalWidget_15")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.horizontalWidget_15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.horizontalWidget_15)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.verticalLayout_13.addWidget(self.horizontalWidget_15)
        self.widget_32 = QtWidgets.QWidget(self.bill_container)
        self.widget_32.setObjectName("widget_32")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_32)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget_8 = QtWidgets.QWidget(self.widget_32)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.widget_8)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.room_price_lb = QtWidgets.QLabel(self.widget_8)
        self.room_price_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.room_price_lb.setObjectName("room_price_lb")
        self.horizontalLayout_7.addWidget(self.room_price_lb)
        self.verticalLayout_12.addWidget(self.widget_8)
        self.widget_12 = QtWidgets.QWidget(self.widget_32)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_6 = QtWidgets.QLabel(self.widget_12)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_15.addWidget(self.label_6)
        self.duration_lb = QtWidgets.QLabel(self.widget_12)
        self.duration_lb.setText("")
        self.duration_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.duration_lb.setObjectName("duration_lb")
        self.horizontalLayout_15.addWidget(self.duration_lb)
        self.verticalLayout_12.addWidget(self.widget_12)
        self.widget_15 = QtWidgets.QWidget(self.widget_32)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_29 = QtWidgets.QLabel(self.widget_15)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_20.addWidget(self.label_29)
        self.room_total_price_lb = QtWidgets.QLabel(self.widget_15)
        self.room_total_price_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.room_total_price_lb.setObjectName("room_total_price_lb")
        self.horizontalLayout_20.addWidget(self.room_total_price_lb)
        self.verticalLayout_12.addWidget(self.widget_15)
        self.widget_14 = QtWidgets.QWidget(self.widget_32)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_27 = QtWidgets.QLabel(self.widget_14)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_19.addWidget(self.label_27)
        self.service_total_price_lb = QtWidgets.QLabel(self.widget_14)
        self.service_total_price_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.service_total_price_lb.setObjectName("service_total_price_lb")
        self.horizontalLayout_19.addWidget(self.service_total_price_lb)
        self.verticalLayout_12.addWidget(self.widget_14)
        self.widget_23 = QtWidgets.QWidget(self.widget_32)
        self.widget_23.setObjectName("widget_23")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_23)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_28 = QtWidgets.QLabel(self.widget_23)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_22.addWidget(self.label_28)
        self.prepaid_lb = QtWidgets.QLabel(self.widget_23)
        self.prepaid_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.prepaid_lb.setObjectName("prepaid_lb")
        self.horizontalLayout_22.addWidget(self.prepaid_lb)
        self.verticalLayout_12.addWidget(self.widget_23)
        self.line = QtWidgets.QFrame(self.widget_32)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_12.addWidget(self.line)
        self.widget_13 = QtWidgets.QWidget(self.widget_32)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_25 = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_18.addWidget(self.label_25)
        self.total_price_lb = QtWidgets.QLabel(self.widget_13)
        self.total_price_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.total_price_lb.setObjectName("total_price_lb")
        self.horizontalLayout_18.addWidget(self.total_price_lb)
        self.verticalLayout_12.addWidget(self.widget_13)
        self.verticalLayout_13.addWidget(self.widget_32)
        self.verticalLayout.addWidget(self.bill_container)
        self.widget_16 = QtWidgets.QWidget(self.verticalWidget)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout.addWidget(self.widget_16)
        self.service_container = QtWidgets.QWidget(self.verticalWidget)
        self.service_container.setStyleSheet("")
        self.service_container.setObjectName("service_container")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.service_container)
        self.horizontalLayout_12.setContentsMargins(0, 10, 10, 0)
        self.horizontalLayout_12.setSpacing(9)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.ok_btn = QtWidgets.QPushButton(self.service_container)
        self.ok_btn.setFlat(True)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_12.addWidget(self.ok_btn)
        self.verticalLayout.addWidget(self.service_container)
        self.verticalLayout_4.addWidget(self.verticalWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_16.addWidget(self.scrollArea)

        self.retranslateUi(Detail_Invoice_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Detail_Invoice_Dialog)

    def retranslateUi(self, Detail_Invoice_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Detail_Invoice_Dialog.setWindowTitle(_translate("Detail_Invoice_Dialog", "Detail Invoice Dialog"))
        self.label_lb.setText(_translate("Detail_Invoice_Dialog", "Personal Information"))
        self.label_4.setText(_translate("Detail_Invoice_Dialog", "Phone:"))
        self.label_3.setText(_translate("Detail_Invoice_Dialog", "Name:"))
        self.label_16.setText(_translate("Detail_Invoice_Dialog", "Service"))
        self.label_18.setText(_translate("Detail_Invoice_Dialog", "Bill"))
        self.label_15.setText(_translate("Detail_Invoice_Dialog", "Room Price"))
        self.room_price_lb.setText(_translate("Detail_Invoice_Dialog", "TextLabel"))
        self.label_6.setText(_translate("Detail_Invoice_Dialog", "Duration"))
        self.label_29.setText(_translate("Detail_Invoice_Dialog", "Room Total Price"))
        self.room_total_price_lb.setText(_translate("Detail_Invoice_Dialog", "TextLabel"))
        self.label_27.setText(_translate("Detail_Invoice_Dialog", "Service Total Price"))
        self.service_total_price_lb.setText(_translate("Detail_Invoice_Dialog", "TextLabel"))
        self.label_28.setText(_translate("Detail_Invoice_Dialog", "Prepaid"))
        self.prepaid_lb.setText(_translate("Detail_Invoice_Dialog", "TextLabel"))
        self.label_25.setText(_translate("Detail_Invoice_Dialog", "Total Price"))
        self.total_price_lb.setText(_translate("Detail_Invoice_Dialog", "TextLabel"))
        self.ok_btn.setText(_translate("Detail_Invoice_Dialog", "Ok"))
