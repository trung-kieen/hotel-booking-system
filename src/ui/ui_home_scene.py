# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/trungkieen/project/hotel-booking-system/src/ui/ui_home_scene.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeScene(object):
    def setupUi(self, HomeScene):
        HomeScene.setObjectName("HomeScene")
        HomeScene.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(HomeScene)
        self.gridLayout.setObjectName("gridLayout")
        self.containerQwidget = QtWidgets.QScrollArea(HomeScene)
        self.containerQwidget.setWidgetResizable(True)
        self.containerQwidget.setObjectName("containerQwidget")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 576))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.summaryContainer = QtWidgets.QVBoxLayout()
        self.summaryContainer.setObjectName("summaryContainer")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.summaryContainer.addWidget(self.label_2)
        self.subdataContainer = QtWidgets.QGridLayout()
        self.subdataContainer.setObjectName("subdataContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.lblTotalCustomer = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblTotalCustomer.setObjectName("lblTotalCustomer")
        self.verticalLayout_2.addWidget(self.lblTotalCustomer)
        self.subdataContainer.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lblAvailableRoom = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblAvailableRoom.setObjectName("lblAvailableRoom")
        self.verticalLayout_3.addWidget(self.lblAvailableRoom)
        self.subdataContainer.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.lblTotalReservation = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblTotalReservation.setObjectName("lblTotalReservation")
        self.verticalLayout_4.addWidget(self.lblTotalReservation)
        self.subdataContainer.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.lblTodayRevenue = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblTodayRevenue.setObjectName("lblTodayRevenue")
        self.verticalLayout_5.addWidget(self.lblTodayRevenue)
        self.subdataContainer.addLayout(self.verticalLayout_5, 1, 1, 1, 1)
        self.summaryContainer.addLayout(self.subdataContainer)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.summaryContainer.addItem(spacerItem)
        self.verticalLayout.addLayout(self.summaryContainer)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setBaseSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.bookingChart = QtWidgets.QGridLayout()
        self.bookingChart.setObjectName("bookingChart")
        self.verticalLayout_6.addLayout(self.bookingChart)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.rdMonth = QtWidgets.QRadioButton(self.groupBox)
        self.rdMonth.setGeometry(QtCore.QRect(110, 10, 95, 26))
        self.rdMonth.setObjectName("rdMonth")
        self.rdQuarter = QtWidgets.QRadioButton(self.groupBox)
        self.rdQuarter.setGeometry(QtCore.QRect(220, 10, 95, 26))
        self.rdQuarter.setObjectName("rdQuarter")
        self.rdYear = QtWidgets.QRadioButton(self.groupBox)
        self.rdYear.setGeometry(QtCore.QRect(330, 10, 95, 26))
        self.rdYear.setObjectName("rdYear")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(30, 10, 71, 17))
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.groupBox)
        self.revenueChart = QtWidgets.QGridLayout()
        self.revenueChart.setObjectName("revenueChart")
        self.verticalLayout_8.addLayout(self.revenueChart)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.containerQwidget.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.containerQwidget, 0, 0, 1, 1)

        self.retranslateUi(HomeScene)
        QtCore.QMetaObject.connectSlotsByName(HomeScene)

    def retranslateUi(self, HomeScene):
        _translate = QtCore.QCoreApplication.translate
        HomeScene.setWindowTitle(_translate("HomeScene", "Hotel"))
        self.label_2.setText(_translate("HomeScene", "General"))
        self.label_5.setText(_translate("HomeScene", "Total customer (up to now)"))
        self.lblTotalCustomer.setText(_translate("HomeScene", "150"))
        self.label.setText(_translate("HomeScene", "Total room (can be use/total)"))
        self.lblAvailableRoom.setText(_translate("HomeScene", "100/200"))
        self.label_6.setText(_translate("HomeScene", "Total reservation up to now (success/cancel/total)"))
        self.lblTotalReservation.setText(_translate("HomeScene", "200"))
        self.label_9.setText(_translate("HomeScene", "Today revenue"))
        self.lblTodayRevenue.setText(_translate("HomeScene", "2000"))
        self.label_10.setText(_translate("HomeScene", "Today reservation"))
        self.label_11.setText(_translate("HomeScene", "Revenue statistic"))
        self.rdMonth.setText(_translate("HomeScene", "1 month"))
        self.rdQuarter.setText(_translate("HomeScene", "3 month"))
        self.rdYear.setText(_translate("HomeScene", "year"))
        self.label_12.setText(_translate("HomeScene", "Group by"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeScene = QtWidgets.QWidget()
    ui = Ui_HomeScene()
    ui.setupUi(HomeScene)
    HomeScene.show()
    sys.exit(app.exec_())
