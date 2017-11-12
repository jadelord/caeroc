# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CalcDialog(object):
    def setupUi(self, CalcDialog):
        CalcDialog.setObjectName("CalcDialog")
        CalcDialog.resize(459, 692)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CalcDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridWidget = QtWidgets.QWidget(CalcDialog)
        self.gridWidget.setObjectName("gridWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gridWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.valueFrame = QtWidgets.QFrame(self.gridWidget)
        self.valueFrame.setObjectName("valueFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.valueFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.modeFrame = QtWidgets.QFrame(self.valueFrame)
        self.modeFrame.setObjectName("modeFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.modeFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.qrb4_obli = QtWidgets.QRadioButton(self.modeFrame)
        self.qrb4_obli.setObjectName("qrb4_obli")
        self.gridLayout_2.addWidget(self.qrb4_obli, 3, 2, 1, 1)
        self.qrb3_norm = QtWidgets.QRadioButton(self.modeFrame)
        self.qrb3_norm.setObjectName("qrb3_norm")
        self.gridLayout_2.addWidget(self.qrb3_norm, 2, 2, 1, 1)
        self.qrb1_isen = QtWidgets.QRadioButton(self.modeFrame)
        self.qrb1_isen.setChecked(True)
        self.qrb1_isen.setObjectName("qrb1_isen")
        self.gridLayout_2.addWidget(self.qrb1_isen, 2, 1, 1, 1)
        self.qrb5_fann = QtWidgets.QRadioButton(self.modeFrame)
        self.qrb5_fann.setObjectName("qrb5_fann")
        self.gridLayout_2.addWidget(self.qrb5_fann, 2, 3, 1, 1)
        self.qrb6_rayl = QtWidgets.QRadioButton(self.modeFrame)
        self.qrb6_rayl.setObjectName("qrb6_rayl")
        self.gridLayout_2.addWidget(self.qrb6_rayl, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.modeFrame)
        self.label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 2, 1)
        self.qrb2_expa = QtWidgets.QRadioButton(self.modeFrame)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.qrb2_expa.setFont(font)
        self.qrb2_expa.setObjectName("qrb2_expa")
        self.gridLayout_2.addWidget(self.qrb2_expa, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.modeFrame, 0, 0, 1, 2)
        self.inputFrame = QtWidgets.QFrame(self.valueFrame)
        self.inputFrame.setObjectName("inputFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.inputFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.qcb1_input = QtWidgets.QComboBox(self.inputFrame)
        self.qcb1_input.setObjectName("qcb1_input")
        self.gridLayout_3.addWidget(self.qcb1_input, 5, 3, 1, 1)
        self.formFrame = QtWidgets.QFrame(self.inputFrame)
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.qcb_autocalc = QtWidgets.QCheckBox(self.formFrame)
        self.qcb_autocalc.setObjectName("qcb_autocalc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.qcb_autocalc)
        self.qpb_calculate = QtWidgets.QPushButton(self.formFrame)
        self.qpb_calculate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.qpb_calculate.setAutoFillBackground(False)
        self.qpb_calculate.setObjectName("qpb_calculate")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.qpb_calculate)
        self.gridLayout_3.addWidget(self.formFrame, 7, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.inputFrame)
        self.label_3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 5, 0, 2, 1)
        self.qdsb2_input = QtWidgets.QDoubleSpinBox(self.inputFrame)
        self.qdsb2_input.setDecimals(8)
        self.qdsb2_input.setMinimum(-99.0)
        self.qdsb2_input.setSingleStep(0.1)
        self.qdsb2_input.setProperty("value", 0.0)
        self.qdsb2_input.setObjectName("qdsb2_input")
        self.gridLayout_3.addWidget(self.qdsb2_input, 6, 4, 1, 1)
        self.qcb2_input = QtWidgets.QComboBox(self.inputFrame)
        self.qcb2_input.setObjectName("qcb2_input")
        self.gridLayout_3.addWidget(self.qcb2_input, 6, 3, 1, 1)
        self.qdsb1_input = QtWidgets.QDoubleSpinBox(self.inputFrame)
        self.qdsb1_input.setDecimals(8)
        self.qdsb1_input.setMaximum(999.99)
        self.qdsb1_input.setSingleStep(0.1)
        self.qdsb1_input.setProperty("value", 1.0)
        self.qdsb1_input.setObjectName("qdsb1_input")
        self.gridLayout_3.addWidget(self.qdsb1_input, 5, 4, 1, 1)
        self.qdsb_gamma = QtWidgets.QDoubleSpinBox(self.inputFrame)
        self.qdsb_gamma.setSingleStep(0.1)
        self.qdsb_gamma.setProperty("value", 1.4)
        self.qdsb_gamma.setObjectName("qdsb_gamma")
        self.gridLayout_3.addWidget(self.qdsb_gamma, 7, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.inputFrame)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 7, 0, 1, 1)
        self.gridLayout.addWidget(self.inputFrame, 2, 0, 4, 2)
        self.verticalLayout.addWidget(self.valueFrame)
        self.outputLayout = QtWidgets.QGridLayout()
        self.outputLayout.setObjectName("outputLayout")
        self.label_4 = QtWidgets.QLabel(self.gridWidget)
        self.label_4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setAcceptDrops(False)
        self.label_4.setObjectName("label_4")
        self.outputLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.qtw_output = QtWidgets.QTableView(self.gridWidget)
        self.qtw_output.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qtw_output.sizePolicy().hasHeightForWidth())
        self.qtw_output.setSizePolicy(sizePolicy)
        self.qtw_output.setAutoFillBackground(False)
        self.qtw_output.setFrameShape(QtWidgets.QFrame.Box)
        self.qtw_output.setFrameShadow(QtWidgets.QFrame.Plain)
        self.qtw_output.setObjectName("qtw_output")
        self.qtw_output.horizontalHeader().setCascadingSectionResizes(False)
        self.outputLayout.addWidget(self.qtw_output, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.outputLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addWidget(self.gridWidget)

        self.retranslateUi(CalcDialog)
        self.buttonBox.accepted.connect(CalcDialog.accept)
        self.buttonBox.rejected.connect(CalcDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CalcDialog)

    def retranslateUi(self, CalcDialog):
        _translate = QtCore.QCoreApplication.translate
        CalcDialog.setWindowTitle(_translate("CalcDialog", "Caeroc Calculator"))
        CalcDialog.setToolTip(_translate("CalcDialog", "<html><head/><body><p>Input</p></body></html>"))
        self.qrb4_obli.setText(_translate("CalcDialog", "Ob&lique Shock"))
        self.qrb3_norm.setText(_translate("CalcDialog", "&Normal Shock"))
        self.qrb1_isen.setText(_translate("CalcDialog", "Isen&tropic"))
        self.qrb5_fann.setText(_translate("CalcDialog", "Fanno F&low"))
        self.qrb6_rayl.setText(_translate("CalcDialog", "Ra&yleigh Flow"))
        self.label.setToolTip(_translate("CalcDialog", "Choos a formula set"))
        self.label.setText(_translate("CalcDialog", "Mode"))
        self.qrb2_expa.setText(_translate("CalcDialog", "E&xpansion"))
        self.qcb_autocalc.setText(_translate("CalcDialog", "AutoCalculate"))
        self.qpb_calculate.setText(_translate("CalcDialog", "Calculate"))
        self.label_3.setText(_translate("CalcDialog", "Input"))
        self.label_2.setText(_translate("CalcDialog", "ɣ ="))
        self.label_4.setToolTip(_translate("CalcDialog", "Tabulated output"))
        self.label_4.setText(_translate("CalcDialog", "Result"))
