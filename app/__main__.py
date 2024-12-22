import sys
import json

from PyQt6.QtWidgets import QApplication


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("app/cache/user.json", "r") as jsonFile:
        file = json.load(jsonFile)
        if file["is_authorized"]:
            from app.windows.listWindow import ListWindow
            ex = ListWindow()
        else:
            from app.windows.autorisation import Autorisation
            ex = Autorisation()

    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
