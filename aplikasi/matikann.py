# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shutdown.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.Shutdown = QtWidgets.QPushButton(Form)
        self.Shutdown.setGeometry(QtCore.QRect(40, 110, 75, 31))
        self.Shutdown.setObjectName("Shutdown")
        self.Restart = QtWidgets.QPushButton(Form)
        self.Restart.setGeometry(QtCore.QRect(160, 110, 75, 31))
        self.Restart.setObjectName("Restart")
        self.Exit = QtWidgets.QPushButton(Form)
        self.Exit.setGeometry(QtCore.QRect(280, 110, 75, 31))
        self.Exit.setObjectName("Exit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 50, 191, 21))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.Exit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Shutdown.setText(_translate("Form", "Shutdown"))
        self.Restart.setText(_translate("Form", "Restart"))
        self.Exit.setText(_translate("Form", "Exit"))
        self.label.setText(_translate("Form", "PILIH SESUAI KEINGINAN ANDA BOS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

