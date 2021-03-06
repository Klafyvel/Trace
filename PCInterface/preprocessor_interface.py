# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preprocessor.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(690, 296)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("traceIcon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        dialog.setModal(True)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chk_del_num = QtWidgets.QCheckBox(self.groupBox)
        self.chk_del_num.setChecked(True)
        self.chk_del_num.setObjectName("chk_del_num")
        self.verticalLayout.addWidget(self.chk_del_num)
        self.chk_optimize_trace = QtWidgets.QCheckBox(self.groupBox)
        self.chk_optimize_trace.setObjectName("chk_optimize_trace")
        self.verticalLayout.addWidget(self.chk_optimize_trace)
        self.chk_del_comments = QtWidgets.QCheckBox(self.groupBox)
        self.chk_del_comments.setChecked(True)
        self.chk_del_comments.setObjectName("chk_del_comments")
        self.verticalLayout.addWidget(self.chk_del_comments)
        self.chk_do_calcs = QtWidgets.QCheckBox(self.groupBox)
        self.chk_do_calcs.setObjectName("chk_do_calcs")
        self.verticalLayout.addWidget(self.chk_do_calcs)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.btn_run_preproc = QtWidgets.QPushButton(self.widget)
        self.btn_run_preproc.setObjectName("btn_run_preproc")
        self.verticalLayout_3.addWidget(self.btn_run_preproc)
        self.horizontalLayout.addWidget(self.widget)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.output = QtWidgets.QTextEdit(self.groupBox_2)
        self.output.setObjectName("output")
        self.verticalLayout_2.addWidget(self.output)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Préprocesseur"))
        self.groupBox.setTitle(_translate("dialog", "Paramètres"))
        self.chk_del_num.setText(_translate("dialog", "Supprimer la numérotation (NXX)"))
        self.chk_optimize_trace.setToolTip(_translate("dialog", "Non disponible"))
        self.chk_optimize_trace.setText(_translate("dialog", "Optimiser le déplacement entre les traçés"))
        self.chk_del_comments.setText(_translate("dialog", "Supprimer les commentaires"))
        self.chk_do_calcs.setToolTip(_translate("dialog", "Non disponible"))
        self.chk_do_calcs.setText(_translate("dialog", "Effectuer les calculs"))
        self.btn_run_preproc.setText(_translate("dialog", "Lancer le préprocesseur"))
        self.groupBox_2.setTitle(_translate("dialog", "Sortie"))

