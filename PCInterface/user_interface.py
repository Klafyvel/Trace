# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filename = QtWidgets.QLabel(self.groupBox_2)
        self.filename.setObjectName("filename")
        self.horizontalLayout.addWidget(self.filename)
        self.btn_file = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_file.setObjectName("btn_file")
        self.horizontalLayout.addWidget(self.btn_file)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.fileview = QtWidgets.QGraphicsView(self.groupBox_2)
        self.fileview.setObjectName("fileview")
        self.verticalLayout.addWidget(self.fileview)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_serie = QtWidgets.QWidget()
        self.tab_serie.setObjectName("tab_serie")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_serie)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab_serie)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.baudrate = QtWidgets.QComboBox(self.tab_serie)
        self.baudrate.setObjectName("baudrate")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.baudrate)
        self.portSRieLabel = QtWidgets.QLabel(self.tab_serie)
        self.portSRieLabel.setObjectName("portSRieLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.portSRieLabel)
        self.serial_ports_list = QtWidgets.QComboBox(self.tab_serie)
        self.serial_ports_list.setObjectName("serial_ports_list")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.serial_ports_list)
        self.btn_serial_ports_list = QtWidgets.QPushButton(self.tab_serie)
        self.btn_serial_ports_list.setObjectName("btn_serial_ports_list")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_serial_ports_list)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.btn_connect = QtWidgets.QPushButton(self.tab_serie)
        self.btn_connect.setObjectName("btn_connect")
        self.verticalLayout_3.addWidget(self.btn_connect)
        self.tabWidget.addTab(self.tab_serie, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_preprocessor = QtWidgets.QPushButton(self.tab_2)
        self.btn_preprocessor.setObjectName("btn_preprocessor")
        self.verticalLayout_5.addWidget(self.btn_preprocessor)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_y_minus = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_y_minus.setObjectName("btn_y_minus")
        self.gridLayout_2.addWidget(self.btn_y_minus, 2, 1, 1, 1)
        self.btn_x_minus = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_x_minus.setObjectName("btn_x_minus")
        self.gridLayout_2.addWidget(self.btn_x_minus, 1, 0, 1, 1)
        self.btn_y_plus = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_y_plus.setObjectName("btn_y_plus")
        self.gridLayout_2.addWidget(self.btn_y_plus, 0, 1, 1, 1)
        self.btn_x_plus = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_x_plus.setObjectName("btn_x_plus")
        self.gridLayout_2.addWidget(self.btn_x_plus, 1, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.btn_set_origin_plan = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_set_origin_plan.setObjectName("btn_set_origin_plan")
        self.horizontalLayout_2.addWidget(self.btn_set_origin_plan)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8.addWidget(self.groupBox_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_set_z_low = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_set_z_low.setObjectName("btn_set_z_low")
        self.gridLayout_3.addWidget(self.btn_set_z_low, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)
        self.btn_set_z_high = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_set_z_high.setObjectName("btn_set_z_high")
        self.gridLayout_3.addWidget(self.btn_set_z_high, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.slider_z_value = QtWidgets.QSlider(self.groupBox_4)
        self.slider_z_value.setOrientation(QtCore.Qt.Vertical)
        self.slider_z_value.setObjectName("slider_z_value")
        self.gridLayout_3.addWidget(self.slider_z_value, 1, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 1, 2, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_3)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.btn_go_to_zero = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_go_to_zero.sizePolicy().hasHeightForWidth())
        self.btn_go_to_zero.setSizePolicy(sizePolicy)
        self.btn_go_to_zero.setFlat(False)
        self.btn_go_to_zero.setObjectName("btn_go_to_zero")
        self.horizontalLayout_3.addWidget(self.btn_go_to_zero)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_4.addWidget(self.splitter)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.serial_monitor = QtWidgets.QTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serial_monitor.sizePolicy().hasHeightForWidth())
        self.serial_monitor.setSizePolicy(sizePolicy)
        self.serial_monitor.setStyleSheet("background-color:black;\n"
"color: yellow;")
        self.serial_monitor.setObjectName("serial_monitor")
        self.verticalLayout_2.addWidget(self.serial_monitor)
        self.verticalLayout_4.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.slider_z_value.valueChanged['int'].connect(self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Fichier"))
        self.filename.setText(_translate("MainWindow", "Pas de fichier"))
        self.btn_file.setText(_translate("MainWindow", "Modifier le fichier"))
        self.pushButton_2.setText(_translate("MainWindow", "Envoyer"))
        self.label.setText(_translate("MainWindow", "Baudrate"))
        self.baudrate.setItemText(0, _translate("MainWindow", "300"))
        self.baudrate.setItemText(1, _translate("MainWindow", "1200"))
        self.baudrate.setItemText(2, _translate("MainWindow", "2400"))
        self.baudrate.setItemText(3, _translate("MainWindow", "4800"))
        self.baudrate.setItemText(4, _translate("MainWindow", "9600"))
        self.baudrate.setItemText(5, _translate("MainWindow", "19200"))
        self.baudrate.setItemText(6, _translate("MainWindow", "38400"))
        self.baudrate.setItemText(7, _translate("MainWindow", "57600"))
        self.baudrate.setItemText(8, _translate("MainWindow", "115200"))
        self.baudrate.setItemText(9, _translate("MainWindow", "230400"))
        self.baudrate.setItemText(10, _translate("MainWindow", "250000"))
        self.portSRieLabel.setText(_translate("MainWindow", "Port série"))
        self.btn_serial_ports_list.setText(_translate("MainWindow", "Lister les ports série"))
        self.btn_connect.setText(_translate("MainWindow", "Connecter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_serie), _translate("MainWindow", "Port série"))
        self.btn_preprocessor.setText(_translate("MainWindow", "Utiliser le préprocesseur sur le fichier"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Paramètres du fichier"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Position dans le plan"))
        self.btn_y_minus.setText(_translate("MainWindow", "Y-"))
        self.btn_x_minus.setText(_translate("MainWindow", "X-"))
        self.btn_y_plus.setText(_translate("MainWindow", "Y+"))
        self.btn_x_plus.setText(_translate("MainWindow", "X+"))
        self.btn_set_origin_plan.setText(_translate("MainWindow", "Position Zéro"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Axe Z"))
        self.btn_set_z_low.setText(_translate("MainWindow", "Position basse"))
        self.label_3.setText(_translate("MainWindow", "0%"))
        self.btn_set_z_high.setText(_translate("MainWindow", "Position haute"))
        self.label_2.setText(_translate("MainWindow", "100%"))
        self.btn_go_to_zero.setText(_translate("MainWindow", "Position Zéro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Contrôles"))
        self.groupBox.setTitle(_translate("MainWindow", "Moniteur série"))
        self.serial_monitor.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

