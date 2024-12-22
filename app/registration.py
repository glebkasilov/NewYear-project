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
            self.output_text.setText('Enter all fields')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

            return

        elif password != password2:
            self.output_text.setText('Passwords do not match')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

            return

        elif email in UserRepository.get_emails():
            self.output_text.setText('User already exists')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
            return

        else:
            UserRepository.create_user(email, password)
            
            self.output_text.setText('Success')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

            from __main__ import Autorisation   
            self.window = Autorisation()
            self.window.show()
            Registr_Window.close(self)

    def enter_login(self):
        from __main__ import Autorisation
        self.window = Autorisation()
        self.window.show()
        Registr_Window.close(self)