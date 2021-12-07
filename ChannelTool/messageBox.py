# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messageBox.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(473, 237)
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(270, 180, 100, 38))
        self.cancel_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(218, 218, 218);\n"
"border-radius:10px;")
        self.cancel_btn.setObjectName("cancel_btn")
        self.content_lable = QtWidgets.QLabel(Dialog)
        self.content_lable.setGeometry(QtCore.QRect(50, 30, 380, 120))
        self.content_lable.setMinimumSize(QtCore.QSize(380, 120))
        self.content_lable.setStyleSheet("font: 16pt \"Microsoft YaHei UI\";")
        self.content_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.content_lable.setObjectName("content_lable")
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(110, 180, 100, 38))
        self.ok_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"color:#fff;\n"
"background-color:#455ab3;color:#fff;\n"
"border-radius:10px;")
        self.ok_btn.setObjectName("ok_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel_btn.setText(_translate("Dialog", "取消"))
        self.content_lable.setText(_translate("Dialog", "TextLabel"))
        self.ok_btn.setText(_translate("Dialog", "确定"))

