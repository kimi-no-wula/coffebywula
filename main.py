import sys

import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Coffee description')
        self.con = sqlite3.connect('coffee.sqlite')
        style = f"background-color:rgb{50, 50, 50}"
        self.centralWidget().setStyleSheet(style)
        self.statusbar.setStyleSheet(style)
        self.initUI()

    def initUI(self):
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM Coffee""").fetchall()
        self.coffeeView.setColumnCount(len(result[0]))
        self.coffeeView.setRowCount(0)

        for i, row in enumerate(result):
            self.coffeeView.setRowCount(
                self.coffeeView.rowCount() + 1)
            for j, obj in enumerate(row):
                self.coffeeView.setItem(
                    i, j, QTableWidgetItem(str(obj)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
