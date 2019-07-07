# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Shutdown.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
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

        self.retranslateUi(Form)
        self.Exit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Shutdown.clicked.connect(self.Shutdown1)
        self.Restart.clicked.connect(self.Restart1)

    def Shutdown1(self):
        os.system("Shutdown /s /t 1")

    def Restart1(self):
        os.system("Shutdown /r /t 1")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Shutdown.setText(_translate("Form", "Shutdown"))
        self.Restart.setText(_translate("Form", "Restart"))
        self.Exit.setText(_translate("Form", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
