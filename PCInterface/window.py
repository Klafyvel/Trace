import serial

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from user_interface import Ui_MainWindow

from serial_list import serial_ports

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.file = ""
        self.serial = serial.Serial()

        self.btn_serial_ports_list.clicked.connect(self.list_serials)
        self.btn_connect.clicked.connect(self.connect_serial_manager)

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
    def connect_serial_manager(self):
        if self.serial.isOpen():
            self.serial.close()
            self.baudrate.setEnabled(True)
            self.serial_ports_list.setEnabled(True)
            self.btn_serial_ports_list.setEnabled(True)
            self.btn_connect.setText("Connecter")
            QMessageBox.information(self, "Port série", "Le port série a été fermé.")
            return
        self.serial.port = self.serial_ports_list.currentText()
        self.serial.baudrate = int(self.baudrate.currentText())
        try:
            self.serial.open()
            QMessageBox.information(self, "Port série", "Le port {} a été ouvert à {} bauds".format(self.serial.port, str(self.serial.baudrate)))
            self.baudrate.setEnabled(False)
            self.serial_ports_list.setEnabled(False)
            self.btn_serial_ports_list.setEnabled(False)
            self.btn_connect.setText("Déconnecter")
        except serial.serialutil.SerialException:
            QMessageBox.warning(self, "Port série", "Le port série n'a pas pu être ouvert.")
    
