from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from progress import Ui_Dialog


class MyProgress(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.progress_bar.setValue(0)
        self.content = ""
        self.setupUi(self)
        self.setWindowTitle('进度')
        self.isShow = False

    def setContent(self, title, content):
        self.content = content
        self.setWindowTitle(title)
        self.content_lable.setText(self.content)

    def setValue(self, value):
        self.progress_bar.setValue(value)

    def getValue(self):
        return self.progress_bar.value()

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()

    def showEvent(self, QShowEvent):
        self.isShow = True

    def hideEvent(self, *args, **kwargs):
        self.isShow = False




