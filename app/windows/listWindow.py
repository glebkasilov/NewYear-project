import json

from PyQt6 import uic, QtGui
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QDialog

from app.database.repository import GiftsRepository


class ListWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        with open("app/cache/user.json", "r") as jsonFile:
            file = json.load(jsonFile)
            self.user_email = file["user_email"]

        uic.loadUi('app/style/table.ui', self)
        
        self.updateTable()
        
        self.textEmail.setText("Ваша почта: " + self.user_email)
        self.updateButton.clicked.connect(self.updateTable)
        self.actionOpen_login_window.triggered.connect(self.exit_from_account)
        
        self.addElement.clicked.connect(self.open_window_adding_gift)

    def updateTable(self):
        self.table.setColumnCount(5)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(['Название', 'Количество', 'Цена', "Описание", "Статус"])
        
        total_width = self.table.width()
        num_cols = self.table.columnCount()
        col_width = [200, 75, 75, 630, 80]

        for i in range(num_cols):
            self.table.setColumnWidth(i, col_width[i])
        
        lists = GiftsRepository.get_list(self.user_email)

        for i, list in enumerate(lists):
            self.table.insertRow(i)
            list = [list[0], list[1], list[2], list[3], "Купленно" if list[4] else "Не купленно"]
            
            for j, item in enumerate(list):
                self.table.setItem(i, j, QTableWidgetItem(str(item)))

        # self.table.resizeColumnsToContents()
        # self.table.resizeRowsToContents()
    
    def exit_from_account(self):
        with open("app/cache/user.json", "w") as jsonFile:
            json.dump({"user_email": "", "is_authorized": False}, jsonFile)

        from app.windows.autorisation import Autorisation
        self.window = Autorisation()
        self.window.show()
        ListWindow.close(self)
    
    def open_window_adding_gift(self):
        from app.windows.dialog.add_gift import AddGift
        self.window = AddGift(self.user_email)
        self.window.show()