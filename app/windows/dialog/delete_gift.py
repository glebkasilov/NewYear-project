from PyQt6 import uic, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog

from app.database.repository import GiftsRepository


class DeleteGift(QDialog):
    def __init__(self, email):
        super().__init__()
        uic.loadUi('app/style/dialog/delete_gift.ui', self)
        self.email = email
        self.show()

        self.deleteList.addItems(GiftsRepository.get_list_of_names(self.email))

        self.deleteButton.clicked.connect(self.delete)
        self.cancelButton.clicked.connect(self.close)

    def delete(self):
        name = self.deleteList.currentText()

        GiftsRepository.delete_list(self.email, name)

        self.close()
