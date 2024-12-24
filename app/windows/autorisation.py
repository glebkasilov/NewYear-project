import json

from PyQt6 import uic, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow

from app.database.repository import UserRepository


class Autorisation(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('app/style/login.ui', self)
        
        self.logo.setPixmap(QtGui.QPixmap('app/photos/logo.png'))
        self.logo.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.pictureQ.setPixmap(QtGui.QPixmap('app/photos/listback.jpg'))

        self.actionOpen_window_registration.triggered.connect(
            self.registration_window)

        self.enter_button.clicked.connect(self.enter)

    def enter(self):
        email = self.input_login.text()
        password = self.input_password.text()

        user = UserRepository.get_users()

        if email == "" and password == "":
            self.output_text.setText('Введите почту и пароль')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        elif email == "" and password != "":
            self.output_text.setText('Введите почту')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        elif email != "" and password == "":
            self.output_text.setText('Введите пароль')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        elif email not in UserRepository.get_emails():
            self.output_text.setText('Пользователь не найден')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        else:
            user = UserRepository.get_user(email)

            if user[0] == email and user[1] == password:
                self.output_text.setText('Что-то пошло не так')
                self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
                self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

                with open("app/cache/user.json", "r") as jsonFile:
                    file = json.load(jsonFile)
                    file["user_email"] = email
                    file["is_authorized"] = True

                with open("app/cache/user.json", "w") as jsonFile:
                    json.dump(file, jsonFile)

                from app.windows.listWindow import ListWindow

                self.main_window = ListWindow()

                self.main_window.show()
                self.close()

            else:
                self.output_text.setText('Неверный пароль')
                self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
                self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def registration_window(self):
        from app.windows.registration import Registr_Window

        self.registration_wn = Registr_Window()
        self.registration_wn.show()
        Autorisation.hide(self)

    def registration_window(self):
        from app.windows.registration import Registr_Window

        self.registration_wn = Registr_Window()
        self.registration_wn.show()
        Autorisation.hide(self)
