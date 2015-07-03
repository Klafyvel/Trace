from PyQt5.QtWidgets import QMainWindow
from user_interface import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    @pyqtSlot()
    def choose_file(self):
        #todo
