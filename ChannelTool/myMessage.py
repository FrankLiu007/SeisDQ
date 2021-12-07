from PyQt5.QtWidgets import QMessageBox, QDialog

from messageBox import Ui_Dialog


class MyMessageBox(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.reply = QMessageBox.Close
        self.content = ""
        self.setupUi(self)
        self.setWindowTitle('提示')
        self.ok_btn.clicked.connect(self.ok_click)
        self.cancel_btn.clicked.connect(self.cancel_click)

    def ok_click(self):
        self.reply = QMessageBox.Ok
        self.content = ""
        self.content_lable.setText(self.content)
        self.close()

    def cancel_click(self):
        self.reply = QMessageBox.Cancel
        self.content = ""
        self.content_lable.setText(self.content)
        self.close()

    def setContent(self, title, content):
        self.content = content
        self.setWindowTitle(title)
        self.content_lable.setText(self.content)
