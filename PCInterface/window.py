import serial

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from user_interface import Ui_MainWindow

from serial_list import serial_ports

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.file = ""
        self.serial = serial.Serial()

        self.btn_serial_ports_list.clicked.connect(self.list_serials)

    @pyqtSlot()
    def choose_file(self):
        pass
    @pyqtSlot()
    def list_serials(self):
        l = serial_ports()
        for i in range(self.serial_ports_list.count()):
            self.serial_ports_list.removeItem(0)
        for i in l:
            self.serial_ports_list.addItem(i)
    @pyqtSlot()
    def connect_serial(self):
        pass
    
