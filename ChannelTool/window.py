# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 671)
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
        self.read_excel_btn = QtWidgets.QPushButton(self.frame)
        self.read_excel_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.read_excel_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(226,226,226);")
        self.read_excel_btn.setObjectName("read_excel_btn")
        self.horizontalLayout.addWidget(self.read_excel_btn)
        self.crawl_btn = QtWidgets.QPushButton(self.frame)
        self.crawl_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.crawl_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color:#455ab3;\n"
"color:#fff;")
        self.crawl_btn.setObjectName("crawl_btn")
        self.horizontalLayout.addWidget(self.crawl_btn)
        self.verticalLayout.addWidget(self.frame)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setSpacing(30)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.staion_info_path_edit = QtWidgets.QLineEdit(self.frame_9)
        self.staion_info_path_edit.setMinimumSize(QtCore.QSize(300, 30))
        self.staion_info_path_edit.setStyleSheet("font: 9pt \"Microsoft YaHei UI\";")
        self.staion_info_path_edit.setObjectName("staion_info_path_edit")
        self.horizontalLayout_6.addWidget(self.staion_info_path_edit)
        self.load_btn = QtWidgets.QPushButton(self.frame_9)
        self.load_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.load_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color:#455ab3;\n"
"color:#fff;")
        self.load_btn.setObjectName("load_btn")
        self.horizontalLayout_6.addWidget(self.load_btn)
        self.verticalLayout.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
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
        self.treeWidget.setColumnCount(0)
        self.treeWidget.setObjectName("treeWidget")
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
        self.stationListWidget = QtWidgets.QListWidget(self.frame_3)
        self.stationListWidget.setObjectName("stationListWidget")
        self.verticalLayout_2.addWidget(self.stationListWidget)
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
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout.addWidget(self.frame_7)
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(10, 10))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.save_btn = QtWidgets.QPushButton(self.horizontalFrame)
        self.save_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.save_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color:#455ab3;\n"
"color:#fff;")
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_5.addWidget(self.save_btn)
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.export_cmp_btn = QtWidgets.QPushButton(self.horizontalFrame)
        self.export_cmp_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.export_cmp_btn.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";\n"
"background-color:#455ab3;\n"
"color:#fff;")
        self.export_cmp_btn.setObjectName("export_cmp_btn")
        self.horizontalLayout_5.addWidget(self.export_cmp_btn)
        self.verticalLayout.addWidget(self.horizontalFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Component Select Tool for SeisDQ"))
        self.read_excel_btn.setText(_translate("MainWindow", "选择台站参数文件"))
        self.crawl_btn.setText(_translate("MainWindow", "开始爬取"))
        self.load_btn.setText(_translate("MainWindow", "加载台站数据"))
        self.desc_label.setText(_translate("MainWindow", "network:\n"
"station:"))
        self.prior_btn.setText(_translate("MainWindow", "上一个（Ctrl+A）"))
        self.next_btn.setText(_translate("MainWindow", "下一个（Ctrl+D）"))
        self.save_btn.setText(_translate("MainWindow", "保存所有台站（包含选择）"))
        self.export_cmp_btn.setText(_translate("MainWindow", "导出所有选中分量"))
