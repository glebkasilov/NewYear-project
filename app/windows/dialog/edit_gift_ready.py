from PyQt6 import uic, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox

from app.database.repository import GiftsRepository


class EditGiftReady(QDialog):
    def __init__(self, email):
        super().__init__()
        uic.loadUi('app/style/dialog/edit_gift_ready.ui', self)
        self.email = email
        self.show()

        self.editItems.addItems(GiftsRepository.get_list_of_names(self.email))

        self.okButton.clicked.connect(self.enter)
        self.cancelButton.clicked.connect(self.close)

    def enter(self):
        GiftsRepository.update_isReady(
            self.email, self.editItems.currentText())
        print(self.editItems.currentText())
        self.close()
