#! /usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from window import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    window = QMainWindow()
    ui.setupUi(window)

    window.show()
    app.exec()
