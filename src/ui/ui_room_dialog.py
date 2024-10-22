# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kai/project/hotel-management/src/ui/ui_room_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 449)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 531, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbRoomId = QtWidgets.QLabel(self.layoutWidget)
        self.lbRoomId.setObjectName("lbRoomId")
        self.verticalLayout.addWidget(self.lbRoomId)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cmbFloor = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbFloor.setObjectName("cmbFloor")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbFloor)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtPrice = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtPrice.setInputMask("")
        self.txtPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtPrice.setObjectName("txtPrice")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtPrice)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cmbRoomType = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbRoomType.setObjectName("cmbRoomType")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cmbRoomType)
        self.ckLockRoom = QtWidgets.QCheckBox(self.layoutWidget)
        self.ckLockRoom.setObjectName("ckLockRoom")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ckLockRoom)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbRoomId.setText(_translate("Dialog", "Room details"))
        self.label.setText(_translate("Dialog", "Floor"))
        self.label_2.setText(_translate("Dialog", "Price"))
        self.txtPrice.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "Type"))
        self.ckLockRoom.setText(_translate("Dialog", "Lock"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())