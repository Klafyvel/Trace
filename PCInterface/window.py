import serial

from PyQt5.QtCore import *
from PyQt5.QtGui import *
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
        self.btn_command.clicked.connect(self.send_user_cmd)

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
            self.serial_monitor.setText("<p style='color:blue;font-weight:bold;'>Serial port opened.</p>")
        except serial.serialutil.SerialException:
            QMessageBox.critical(self, "Port série", "Le port série n'a pas pu être ouvert.")

    def send_user_cmd(self):
        if not self.serial.isOpen():
            QMessageBox.critical(self, "Port série", "Veuillez ouvrir un port série.")
            return
        txt = self.command_edit.text()
        self.serial.write(bytes(txt, encoding="utf-8"))
        self.command_edit.setText("")
        self.serial_monitor.moveCursor(QTextCursor.End)
        self.serial_monitor.insertHtml("\n<br /><span style='color:yellow;'>User: {}</span>".format(txt))
        self.serial_monitor.moveCursor(QTextCursor.End)
