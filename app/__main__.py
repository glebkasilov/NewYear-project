import sys

from PyQt6 import uic, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from app.database.repository import UserRepository


class Autorisation(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('app/style/login.ui', self)

        self.actionOpen_window_registration.triggered.connect(
            self.registration_window)

        # self.logo.setPixmap(QtGui.QPixmap('app/photos/logo.jpg'))

        self.enter_button.clicked.connect(self.enter)

    def enter(self):
        logit = self.input_login.text()
        password = self.input_password.text()

        user = UserRepository.get_users()

        if logit == "" and password == "":
            self.output_text.setText('Enter email and password')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        elif logit == "" and password != "":
            self.output_text.setText('Enter email')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        elif logit != "" and password == "":
            self.output_text.setText('Enter password')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        elif user == None:
            self.output_text.setText('Incorrect email or password')
            self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
            self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        else:
            if user["email"] == email and user["password"] == password:
                self.output_text.setText('Success')
                self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
                self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

                with open('app/settings.txt', 'w') as f:
                    f.write(logit)

                # from app.basic import Main_Window
                # self.main_window = Main_Window()
                self.main_window.show()
                # Window.hide(self)

            else:
                self.output_text.setText('Incorrect email or password')
                self.output_text.setFont(QtGui.QFont('MS Shell Dlg 2', 14))
                self.output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def registration_window(self):
        from app.registration import Registr_Window

        self.registration_wn = Registr_Window()
        self.registration_wn.show()
        Autorisation.hide(self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Autorisation()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())