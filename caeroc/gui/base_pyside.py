# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created: Thu May 28 22:46:16 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CalcDialog(object):
    def setupUi(self, CalcDialog):
        CalcDialog.setObjectName("CalcDialog")
        CalcDialog.resize(439, 570)
        self.buttonBox = QtGui.QDialogButtonBox(CalcDialog)
        self.buttonBox.setGeometry(QtCore.QRect(230, 520, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Reset)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget_2 = QtGui.QWidget(CalcDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 113, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.qvbl_mode = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.qvbl_mode.setContentsMargins(0, 0, 0, 0)
        self.qvbl_mode.setObjectName("qvbl_mode")
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.qvbl_mode.addWidget(self.label)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.qvbl_mode.addWidget(self.line_2)
        self.qrb1_isen = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.qrb1_isen.setChecked(True)
        self.qrb1_isen.setObjectName("qrb1_isen")
        self.qvbl_mode.addWidget(self.qrb1_isen)
        self.qrb2_expa = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.qrb2_expa.setFont(font)
        self.qrb2_expa.setObjectName("qrb2_expa")
        self.qvbl_mode.addWidget(self.qrb2_expa)
        self.qrb3_norm = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.qrb3_norm.setObjectName("qrb3_norm")
        self.qvbl_mode.addWidget(self.qrb3_norm)
        self.qrb4_obli = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.qrb4_obli.setObjectName("qrb4_obli")
        self.qvbl_mode.addWidget(self.qrb4_obli)
        self.qrb5_fann = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.qrb5_fann.setObjectName("qrb5_fann")
        self.qvbl_mode.addWidget(self.qrb5_fann)
        self.qrb6_rayl = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.qrb6_rayl.setObjectName("qrb6_rayl")
        self.qvbl_mode.addWidget(self.qrb6_rayl)
        self.line = QtGui.QFrame(CalcDialog)
        self.line.setGeometry(QtCore.QRect(20, 500, 401, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalFrame = QtGui.QFrame(CalcDialog)
        self.verticalFrame.setGeometry(QtCore.QRect(20, 380, 401, 121))
        self.verticalFrame.setObjectName("verticalFrame")
        self.gridLayout = QtGui.QGridLayout(self.verticalFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setUnderline(False)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.verticalFrame)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 2)
        self.qfl_input = QtGui.QFormLayout()
        self.qfl_input.setObjectName("qfl_input")
        self.qcb1_input = QtGui.QComboBox(self.verticalFrame)
        self.qcb1_input.setObjectName("qcb1_input")
        self.qfl_input.setWidget(0, QtGui.QFormLayout.LabelRole, self.qcb1_input)
        self.qdsb1_input = QtGui.QDoubleSpinBox(self.verticalFrame)
        self.qdsb1_input.setDecimals(8)
        self.qdsb1_input.setMaximum(999.99)
        self.qdsb1_input.setSingleStep(0.1)
        self.qdsb1_input.setProperty("value", 1.0)
        self.qdsb1_input.setObjectName("qdsb1_input")
        self.qfl_input.setWidget(0, QtGui.QFormLayout.FieldRole, self.qdsb1_input)
        self.qdsb2_input = QtGui.QDoubleSpinBox(self.verticalFrame)
        self.qdsb2_input.setDecimals(8)
        self.qdsb2_input.setMinimum(-99.0)
        self.qdsb2_input.setProperty("value", 0.0)
        self.qdsb2_input.setObjectName("qdsb2_input")
        self.qfl_input.setWidget(1, QtGui.QFormLayout.FieldRole, self.qdsb2_input)
        self.qcb2_input = QtGui.QComboBox(self.verticalFrame)
        self.qcb2_input.setObjectName("qcb2_input")
        self.qfl_input.setWidget(1, QtGui.QFormLayout.LabelRole, self.qcb2_input)
        self.gridLayout.addLayout(self.qfl_input, 2, 0, 4, 1)
        self.qpb_calculate = QtGui.QPushButton(self.verticalFrame)
        self.qpb_calculate.setDefault(True)
        self.qpb_calculate.setObjectName("qpb_calculate")
        self.gridLayout.addWidget(self.qpb_calculate, 2, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.verticalFrame)
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 3, 1, 1, 1)
        self.verticalLayoutWidget_3 = QtGui.QWidget(CalcDialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(140, 10, 281, 361))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAcceptDrops(False)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.line_4 = QtGui.QFrame(self.verticalLayoutWidget_3)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.qtw_output = QtGui.QTableView(self.verticalLayoutWidget_3)
        self.qtw_output.setAutoFillBackground(False)
        self.qtw_output.setObjectName("qtw_output")
        self.verticalLayout_3.addWidget(self.qtw_output)
        self.horizontalLayoutWidget = QtGui.QWidget(CalcDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 340, 111, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.qdsb_gamma = QtGui.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.qdsb_gamma.setSingleStep(0.1)
        self.qdsb_gamma.setProperty("value", 1.4)
        self.qdsb_gamma.setObjectName("qdsb_gamma")
        self.horizontalLayout.addWidget(self.qdsb_gamma)

        self.retranslateUi(CalcDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CalcDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CalcDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CalcDialog)

    def retranslateUi(self, CalcDialog):
        CalcDialog.setWindowTitle(QtGui.QApplication.translate("CalcDialog", "Caeroc Calculator", None, QtGui.QApplication.UnicodeUTF8))
        CalcDialog.setToolTip(QtGui.QApplication.translate("CalcDialog", "<html><head/><body><p>Input</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("CalcDialog", "Choos a formula set", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CalcDialog", " Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.qrb1_isen.setText(QtGui.QApplication.translate("CalcDialog", "Isentropic", None, QtGui.QApplication.UnicodeUTF8))
        self.qrb2_expa.setText(QtGui.QApplication.translate("CalcDialog", "Expansion", None, QtGui.QApplication.UnicodeUTF8))
        self.qrb3_norm.setText(QtGui.QApplication.translate("CalcDialog", "Normal Shock", None, QtGui.QApplication.UnicodeUTF8))
        self.qrb4_obli.setText(QtGui.QApplication.translate("CalcDialog", "Oblique Shock", None, QtGui.QApplication.UnicodeUTF8))
        self.qrb5_fann.setText(QtGui.QApplication.translate("CalcDialog", "Fanno Flow", None, QtGui.QApplication.UnicodeUTF8))
        self.qrb6_rayl.setText(QtGui.QApplication.translate("CalcDialog", "Rayleigh Flow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CalcDialog", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.qpb_calculate.setText(QtGui.QApplication.translate("CalcDialog", "Calculate!", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setToolTip(QtGui.QApplication.translate("CalcDialog", "Auto-updates the result as the input is changed", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("CalcDialog", "Auto-Calculate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setToolTip(QtGui.QApplication.translate("CalcDialog", "Tabulated output", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CalcDialog", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CalcDialog", "ɣ =", None, QtGui.QApplication.UnicodeUTF8))
