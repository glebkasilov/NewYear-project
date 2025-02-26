from PyQt6 import uic, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox

from app.database.repository import GiftsRepository


class AddGift(QDialog):
    def __init__(self, email):
        super().__init__()
        uic.loadUi('app/style/dialog/add_gift.ui', self)
        self.email = email
        self.show()

        self.okButton.clicked.connect(self.enter)
        self.cancelButton.clicked.connect(self.close)

    def show_error_message(self, message="Внутряняя ошибка"):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Ошибка")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel)

        msg_box.exec()

    def show_error_message(self, message="Внутряняя ошибка"):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Ошибка")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel)

        msg_box.exec()

    def enter(self):
        name = self.nameInput.text()
        count = self.quantityInput.text()
        price = self.priceInput.text()
        description = self.descriptionInput.toPlainText()

        if name in GiftsRepository.get_list_of_names(self.email):
            self.show_error_message("Такой подарок уже есть")
            return

        if name == "" or count == "" or price == "":
            self.show_error_message("Заполните все поля")
            return

        GiftsRepository.create_list(
            self.email, name, count, price, description, False)

        self.close()
