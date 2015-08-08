from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from preprocessor_interface import Ui_dialog

from gcodeParser import parse_instr

class PreprocessorDialog(QDialog, Ui_dialog):
    def __init__(self, gcode, parent=None):
        super(PreprocessorDialog, self).__init__(parent=parent)
        self.setupUi(self)
        self.gcode = gcode
        self.original = gcode

        self.btn_run_preproc.clicked.connect(self.run_preprocessor)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.cancel)

    @pyqtSlot()
    def run_preprocessor(self):
        self.remove_useless()
    def remove_useless(self):
        rm_nums = self.chk_del_num.isChecked()
        rm_comm = self.chk_del_comments.isChecked()
        r = ''
        for i in parse_instr(self.gcode):
            if 'M' in i['name'] or 'G' in i['name']:
                if not rm_nums and 'N' in i['args']:
                    r += 'N' + str(int(i['args']['N'])) + ' '
                r += i['name'] + str(int(i['value'])) + ' '
                for a in i['args']:
                    if a in 'XYZIJF':
                        r += a + str(i['args'][a]) + ' '
                if 'comment' in i['args'] and not rm_comm:
                    t += '(' + i['args']['comment'] + ')'
                r += '\n'
        self.output.setText(r)
        self.gcode = r

    @pyqtSlot()
    def cancel(self):
        self.gcode = self.original
        self.reject()