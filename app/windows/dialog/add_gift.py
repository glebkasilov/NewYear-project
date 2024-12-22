from PyQt6 import uic, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog

from app.database.repository import GiftsRepository

class AddGift(QDialog):
    def __init__(self, email):
        super().__init__()
        uic.loadUi('app/style/dialog/add_gift.ui', self)
        self.email = email
        self.show()

        self.okButton.clicked.connect(self.enter)
        self.cancelButton.clicked.connect(self.close)

    def enter(self):
        name = self.nameInput.text()
        count = self.quantityInput.text()
        price = self.priceInput.text()
        description = self.descriptionInput.toPlainText()

        GiftsRepository.create_list(self.email, name, count, price, description, False)

        self.close()
        