# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(554, 239)
        self.content_lable = QtWidgets.QLabel(Dialog)
        self.content_lable.setGeometry(QtCore.QRect(29, 30, 481, 60))
        self.content_lable.setMinimumSize(QtCore.QSize(380, 60))
        self.content_lable.setStyleSheet("font: 12pt \"Microsoft YaHei UI\";")
        self.content_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.content_lable.setObjectName("content_lable")
        self.progress_bar = QtWidgets.QProgressBar(Dialog)
        self.progress_bar.setGeometry(QtCore.QRect(20, 140, 511, 20))
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.content_lable.setText(_translate("Dialog", "TextLabel"))

