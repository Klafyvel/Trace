#! /usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec()
    del window
    del app
