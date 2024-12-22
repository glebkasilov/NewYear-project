import json

from PyQt6 import uic, QtGui
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow

from app.database.repository import UserRepository


class Registr_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app/style/registration.ui', self)

        self.logo.setPixmap(QPixmap('app/photos/logo.jpg'))

        self.enter_button.clicked.connect(self.enter)
        self.actionOpen_window_login.triggered.connect(self.enter_login)

    def enter(self):
        email = self.input_login.text()
        password = self.input_password.text()
        password2 = self.input_password_2.text()

        if email == '' or password == '' or password2 == '':
            self.output_text.setText('Заполните все поля')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

            return

        elif password != password2:
            self.output_text.setText('Пароли не совпадают')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

            return

        elif email in UserRepository.get_emails():
            self.output_text.setText('Такая почта уже зарегистрирована')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
            return

        else:
            UserRepository.create_user(email, password)

            self.output_text.setText('Что-то пошло не так')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

            with open('app/cache/user.json', 'r') as jsonFile:
                file = json.load(jsonFile)
                file["user_email"] = email
                file["is_authorized"] = True

            with open('app/cache/user.json', 'w') as jsonFile:
                json.dump(file, jsonFile)

            from app.windows.listWindow import ListWindow
            self.window = ListWindow()
            self.window.show()
            Registr_Window.close(self)

    def enter_login(self):
        from app.windows.autorisation import Autorisation
        self.window = Autorisation()
        self.window.show()
        Registr_Window.close(self)
