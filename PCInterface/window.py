# Trace
# Copyright (C) 2015  Hugo LEVY-FALK
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import serial

from math import asin, acos, sqrt, pi

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from user_interface import Ui_MainWindow

from serial_list import serial_ports

from gcodeParser import parse_instr

from preprocessor import PreprocessorDialog


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.file = ""
        self.serial = serial.Serial(timeout=0.1)

        self.btn_serial_ports_list.clicked.connect(self.list_serials)
        self.btn_connect.clicked.connect(self.connect_serial_manager)
        self.btn_command.clicked.connect(self.send_user_cmd)
        self.btn_file.clicked.connect(self.choose_file)
        self.btn_go_to_zero.clicked.connect(self.go_to_zero)
        self.display_draw_steps.clicked.connect(self.draw_file)
        self.redraw.clicked.connect(self.draw_file)
        self.btn_send_current_file.clicked.connect(self.send_file)
        self.send_manual_cmd.stateChanged.connect(self.manual_mode)
        self.btn_reload.clicked.connect(self.load_file)
        self.btn_save_file.clicked.connect(self.save_file)
        self.btn_save_as.clicked.connect(self.save_as)
        self.btn_preprocessor.clicked.connect(self.preprocessor)

        self.btn_x_plus.clicked.connect(self.x_plus)
        self.btn_x_minus.clicked.connect(self.x_minus)
        self.btn_y_plus.clicked.connect(self.y_plus)
        self.btn_y_minus.clicked.connect(self.y_minus)

        self.btn_set_z_high.clicked.connect(self.z_high)
        self.btn_set_z_low.clicked.connect(self.z_low)

        self.aboutQt.clicked.connect(self.show_Qt)

        self.serial_timer = QTimer()
        self.serial_timer.timeout.connect(self.check_serial_communication)

        self.grp_plan.setEnabled(False)
        self.grp_z.setEnabled(False)
        self.btn_go_to_zero.setEnabled(False)
        self.btn_command.setEnabled(False)
        self.command_edit.setEnabled(False)

        self.pos = [0, 0, 1]

        self.sc = QGraphicsScene(self.fileview)
        self.fileview.scale(1, -1)
        self.preproc = PreprocessorDialog("", parent=self)
        self.preproc.accepted.connect(self.get_preprocessor_result)

        self.list_serials()

    @pyqtSlot()
    def check_serial_communication(self):
        if self.serial.isOpen():
            try:
                txt = self.serial.readline().decode('ascii')
                if txt is not '':
                    self.print(txt, self.MACHINE_PRINT)
            except serial.serialutil.SerialException:
                self.connect_serial_manager()

    @pyqtSlot()
    def choose_file(self):
        t = QFileDialog.getOpenFileName(
            self, "Sélectionner un fichier", filter='Gcodes files (*.gcode *.ngc)\nAll files (*)')[0]
        if t is not '':
            self.file = t
            self.load_file()

    @pyqtSlot()
    def load_file(self):
        if self.file:
            self.filename.setText(self.file)
            with open(self.file, "r") as f:
                self.code_edit.setText(f.read())
            self.draw_file()

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
            self.serial_timer.stop()
            self.serial.close()
            self.baudrate.setEnabled(True)
            self.serial_ports_list.setEnabled(True)
            self.btn_serial_ports_list.setEnabled(True)
            self.timeout_read.setEnabled(True)
            self.btn_connect.setText("Connecter")
            self.send_manual_cmd.setChecked(False)
            QMessageBox.information(
                self, "Port série", "Le port série a été fermé.")
            self.print("Serial port closed", self.INFO_PRINT)
            return
        self.serial.port = self.serial_ports_list.currentText()
        self.serial.baudrate = int(self.baudrate.currentText())
        # serial needs timeout in seconds
        self.serial.timeout = self.timeout_read.value() / 1000
        try:
            self.serial.open()
            QMessageBox.information(self, "Port série", "Le port {} a été ouvert à {} bauds".format(
                self.serial.port, str(self.serial.baudrate)))
            self.baudrate.setEnabled(False)
            self.serial_ports_list.setEnabled(False)
            self.btn_serial_ports_list.setEnabled(False)
            self.timeout_read.setEnabled(False)
            self.btn_connect.setText("Déconnecter")
            self.print("Serial port opened", self.INFO_PRINT)
            self.serial_timer.start(50)
        except serial.serialutil.SerialException:
            QMessageBox.critical(self, "Port série",
                                 "Le port série n'a pas pu être ouvert.")

    def send_user_cmd(self):
        if not self.serial.isOpen():
            QMessageBox.critical(self, "Port série",
                                 "Veuillez ouvrir un port série.")
            return
        txt = self.command_edit.text()
        self.serial.write(bytes(txt + '\n', encoding="utf-8"))
        self.command_edit.setText("")
        self.print(txt, self.USER_PRINT)

    @pyqtSlot()
    def manual_mode(self):
        if self.send_manual_cmd.isChecked():
            if not self.serial.isOpen():
                QMessageBox.critical(self, "Port série",
                                     "Veuillez ouvrir un port série.")
                self.send_manual_cmd.setChecked(False)
                return
            self.print("Start manual mode", self.INFO_PRINT)
            self.serial.write(bytes('prgm', encoding="utf-8"))
            self.grp_plan.setEnabled(True)
            self.grp_z.setEnabled(True)
            self.btn_go_to_zero.setEnabled(True)
            self.btn_command.setEnabled(True)
            self.command_edit.setEnabled(True)
        else:
            self.print("End of manual mode", self.INFO_PRINT)
            self.grp_plan.setEnabled(False)
            self.grp_z.setEnabled(False)
            self.btn_go_to_zero.setEnabled(False)
            self.btn_command.setEnabled(False)
            self.command_edit.setEnabled(False)

    @pyqtSlot()
    def go_to_zero(self):
        self.command_edit.setText("G28")
        self.send_user_cmd()

    @pyqtSlot()
    def y_plus(self):
        self.pos[1] += self.step_y.value()
        self.command_edit.setText("G00 Y{}".format(self.pos[1]))
        self.send_user_cmd()

    @pyqtSlot()
    def y_minus(self):
        self.pos[1] -= self.step_y.value()
        self.command_edit.setText("G00 Y{}".format(self.pos[1]))
        self.send_user_cmd()

    @pyqtSlot()
    def x_plus(self):
        self.pos[0] += self.step_x.value()
        self.command_edit.setText("G00 X{}".format(self.pos[0]))
        self.send_user_cmd()

    @pyqtSlot()
    def x_minus(self):
        self.pos[0] -= self.step_x.value()
        self.command_edit.setText("G00 X{}".format(self.pos[0]))
        self.send_user_cmd()

    @pyqtSlot()
    def z_high(self):
        self.pos[2] = 1
        self.command_edit.setText("G00 Z{}".format(self.pos[2]))
        self.send_user_cmd()

    @pyqtSlot()
    def z_low(self):
        self.pos[2] = -1
        self.command_edit.setText("G00 Z{}".format(self.pos[2]))
        self.send_user_cmd()

    @pyqtSlot()
    def send_file(self):
        if not self.serial.isOpen():
            QMessageBox.critical(self, "Port série",
                                 "Veuillez ouvrir un port série.")
            return
        self.send_manual_cmd.setChecked(False)
        self.serial.write(bytes('prgm', encoding="utf-8"))
        gcode = self.code_edit.toPlainText().split('\n')
        # no timeout while we are working, because we don't know how many time
        # needs the machine.
        self.serial.timeout = None
        for c in gcode:
            self.print(c, self.PRGM_PRINT)
            self.serial.write(bytes(c + '\n', "utf-8"))
            txt = self.serial.readline().decode('ascii')
            self.print(txt, self.MACHINE_PRINT)
            if 'OK' not in txt:
                QMessageBox.critical(self, "Port série",
                                     "Erreur sur la machine.")
                break
        # serial needs timeout in seconds
        self.serial.timeout = self.timeout_read.value() / 1000
        QMessageBox.information(self, "Port série", "Fin de l'usinage.")

    @pyqtSlot()
    def draw_file(self):
        gcode = self.code_edit.toPlainText()
        self.sc.clear()
        current_pos = [0, 0, 0]
        for n, t in enumerate(parse_instr(gcode)):
            if t['name'] is not 'G':
                continue

            x, y, z = current_pos

            if self.display_draw_steps.isChecked():
                txt = self.sc.addText(str(n))
                txt.setPos(x, y)
                txt.setFlags(QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsMovable |
                             QGraphicsItem.ItemIsSelectable | txt.flags())

            x = t['args'].get('X', x)
            y = t['args'].get('Y', y)
            z = t['args'].get('Z', z)

            p = QPen(QColor((z <= 0) * 255, 0, (z > 0) * 255))

            if t['value'] in (0, 1):
                self.sc.addLine(current_pos[0], current_pos[1], x, y, pen=p)
            elif t['value'] in (2, 3):
                i, j, k, = current_pos
                i = t['args'].get('I', i)
                j = t['args'].get('J', j)
                k = t['args'].get('K', k)

                pp = QPainterPath()

                h = sqrt(i**2 + j**2)
                if h == 0:
                    current_pos = x, y, z
                    continue

                center_x = current_pos[0] + i
                center_y = current_pos[1] + j

                clockwise = (t['value'] == 2)

                direction_end = -1
                direction_begin = -1
                if y - center_y != 0:
                    direction_end = -(y - center_y) / abs(y - center_y)
                if current_pos[1] - center_y != 0:
                    direction_begin = - \
                        (current_pos[1] - center_y) / \
                        abs(current_pos[1] - center_y)

                c = (current_pos[0] - center_x) / h
                if c < -1:
                    c = -1
                elif c > 1:
                    c = 1
                start_angle = direction_begin * acos(c) / 2 / pi * 360

                c = (x - center_x) / h
                if c < -1:
                    c = -1
                elif c > 1:
                    c = 1
                end_angle = direction_end * acos(c) / 2 / pi * 360

                pp.moveTo(current_pos[0], current_pos[1])
                if clockwise:
                    pp.arcTo(center_x - h, center_y - h, h * 2, h *
                             2, start_angle, start_angle - end_angle)
                else:
                    pp.arcTo(center_x - h, center_y - h, h * 2, h *
                             2, start_angle, end_angle - start_angle)
                self.sc.addPath(pp, p)
            current_pos = x, y, z

        self.fileview.setScene(self.sc)

    @pyqtSlot()
    def save_file(self):
        if self.file:
            with open(self.file, "w") as f:
                f.write(self.code_edit.toPlainText())
        else:
            self.save_as()

    @pyqtSlot()
    def save_as(self):
        t = QFileDialog.getSaveFileName(
            self, "Sélectionner un fichier", filter='Gcodes files (*.gcode *.ngc)\nAll files (*)')[0]
        if t is not '':
            self.file = t
            self.filename.setText(self.file)
            self.save_file()

    @pyqtSlot()
    def preprocessor(self):
        self.preproc.output.setText('')
        self.preproc.gcode = self.code_edit.toPlainText()
        self.preproc.show()

    @pyqtSlot()
    def get_preprocessor_result(self):
        self.code_edit.setText(self.preproc.gcode)

    @pyqtSlot()
    def show_Qt(self):
        QMessageBox.aboutQt(self)

    USER_PRINT = 0
    INFO_PRINT = 1
    MACHINE_PRINT = 2
    PRGM_PRINT = 3

    def print(self, txt, author=USER_PRINT):
        msg = "{}"
        if author == self.USER_PRINT:
            msg = "\n<br /><span style='color:yellow;'>User: {}</span>"
        elif author == self.INFO_PRINT:
            msg = "\n<br /><span style='color:blue;font-weight:bold;'>{}</span>"
        elif author == self.MACHINE_PRINT:
            msg = "\n<br /><span style='color:green;'>Machine: {}</span>"
        elif author == self.PRGM_PRINT:
            msg = "\n<br /><span style='color:red;'>Prgm: {}</span>"
        self.serial_monitor.moveCursor(QTextCursor.End)
        self.serial_monitor.insertHtml(msg.format(txt))
        self.serial_monitor.moveCursor(QTextCursor.End)
        if self.use_log.isChecked():
            with open("log.txt", 'a') as f:
                f.write(msg.format(txt))
