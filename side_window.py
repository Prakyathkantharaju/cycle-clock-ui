# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'side_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog, main):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(300, 10, 81, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 81, 31))
        self.label_3.setObjectName("label_3")
        self.squat_time = QtWidgets.QTextEdit(Dialog)
        self.squat_time.setGeometry(QtCore.QRect(20, 40, 141, 41))
        self.squat_time.setObjectName("squat_time")
        self.rest_time = QtWidgets.QTextEdit(Dialog)
        self.rest_time.setGeometry(QtCore.QRect(20, 130, 141, 41))
        self.rest_time.setObjectName("rest_time")
        self.no_cycle = QtWidgets.QTextEdit(Dialog)
        self.no_cycle.setGeometry(QtCore.QRect(20, 220, 141, 41))
        self.no_cycle.setObjectName("no_cycle")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(main._read_sub_window)
        self.buttonBox.rejected.connect(main.sub_window.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "squat time"))
        self.label_2.setText(_translate("Dialog", "rest time"))
        self.label_3.setText(_translate("Dialog", "no of cycle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
