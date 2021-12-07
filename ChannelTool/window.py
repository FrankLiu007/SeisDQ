# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 1028)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.excel_path_edit = QtWidgets.QLineEdit(self.frame)
        self.excel_path_edit.setMinimumSize(QtCore.QSize(300, 30))
        self.excel_path_edit.setStyleSheet("font: 9pt \"Microsoft YaHei UI\";")
        self.excel_path_edit.setObjectName("excel_path_edit")
        self.horizontalLayout.addWidget(self.excel_path_edit)
        self.upload_excel_btn = QtWidgets.QPushButton(self.frame)
        self.upload_excel_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.upload_excel_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(226,226,226);")
        self.upload_excel_btn.setObjectName("upload_excel_btn")
        self.horizontalLayout.addWidget(self.upload_excel_btn)
        self.crawl_btn = QtWidgets.QPushButton(self.frame)
        self.crawl_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.crawl_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color:#455ab3;\n"
"color:#fff;")
        self.crawl_btn.setObjectName("crawl_btn")
        self.horizontalLayout.addWidget(self.crawl_btn)
        self.save_btn = QtWidgets.QPushButton(self.frame)
        self.save_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.save_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color:#455ab3;\n"
"color:#fff;")
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.reload_btn = QtWidgets.QPushButton(self.frame)
        self.reload_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.reload_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color:#455ab3;\n"
"color:#fff;")
        self.reload_btn.setObjectName("reload_btn")
        self.horizontalLayout.addWidget(self.reload_btn)
        self.verticalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.horizontalLayout_4.addWidget(self.treeWidget)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.desc_label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.desc_label.setFont(font)
        self.desc_label.setObjectName("desc_label")
        self.verticalLayout_2.addWidget(self.desc_label)
        self.index_label = QtWidgets.QLabel(self.frame_3)
        self.index_label.setMinimumSize(QtCore.QSize(0, 40))
        self.index_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.index_label.setFont(font)
        self.index_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.index_label.setAlignment(QtCore.Qt.AlignCenter)
        self.index_label.setObjectName("index_label")
        self.verticalLayout_2.addWidget(self.index_label)
        self.listWidget = QtWidgets.QListWidget(self.frame_3)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.prior_btn = QtWidgets.QPushButton(self.frame_5)
        self.prior_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(226,226,226);")
        self.prior_btn.setObjectName("prior_btn")
        self.horizontalLayout_3.addWidget(self.prior_btn)
        self.next_btn = QtWidgets.QPushButton(self.frame_5)
        self.next_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(226,226,226);")
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout_3.addWidget(self.next_btn)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.upload_excel_btn.setText(_translate("MainWindow", "参数名上传"))
        self.crawl_btn.setText(_translate("MainWindow", "开始爬取"))
        self.save_btn.setText(_translate("MainWindow", "保  存"))
        self.reload_btn.setText(_translate("MainWindow", "数据加载"))
        self.desc_label.setText(_translate("MainWindow", "network:\n"
"station:"))
        self.index_label.setText(_translate("MainWindow", "0/0"))
        self.prior_btn.setText(_translate("MainWindow", "上一个（Ctrl+A）"))
        self.next_btn.setText(_translate("MainWindow", "下一个（Ctrl+D）"))
