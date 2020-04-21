from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from DataFlowPanel.RSAModule.ui_RSAModule import ui_RSAPanel
from DataFlowPanel.RSAModule.RSAModuleUtils import *
from ui_Widgets.ErrorWin import errorInfo


class RSAPanel(ui_RSAPanel):
    def __init__(self):
        super(RSAPanel, self).__init__()
        self.epqButton.clicked.connect(self.Changeepq)
        self.dnButton.clicked.connect(self.Changedn)
        self.dpdqpqButton.clicked.connect(self.Changedpdqpq)
        self.edpnButton.clicked.connect(self.Changeedpn)
        self.rabinButton.clicked.connect(self.Changerabin)
        # self.RSAEncodeButton.clicked.connect(self.RSAEncode)
        # self.RSADecodeButton.clicked.connect(self.RSADecode)
        # self.RSACipherBox.textChanged.connect(self.setFontColorCipher)
        # self.RSATextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.RSACipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.RSATextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def lableinit(self):
        self.RSAcBox.setEnabled(False)
        self.RSAeBox.setEnabled(False)
        self.RSApBox.setEnabled(False)
        self.RSAqBox.setEnabled(False)
        self.RSAdpBox.setEnabled(False)
        self.RSAdqBox.setEnabled(False)
        self.RSAdBox.setEnabled(False)
        self.RSAmBox.setEnabled(True)
        self.RSAnBox.setEnabled(False)

    def Changeepq(self):
        try:
            animation = Qt.QPropertyAnimation(self)
            animation.setTargetObject(self.RSAChooser)
            animation.setPropertyName(b'pos')
            animation.setStartValue(QtCore.QPoint(
                self.RSAChooserBox[self.RSAMode], 55))
            self.RSAMode = 1

            animation.setEndValue(QtCore.QPoint(
                self.RSAChooserBox[self.RSAMode], 55))
            animation.setDuration(200)
            animation.start()
            self.lableinit()
            self.RSAcBox.setEnabled(True)
            self.RSAeBox.setEnabled(True)
            self.RSApBox.setEnabled(True)
            self.RSAqBox.setEnabled(True)

        except Exception as e:
            print(str(e))

    def Changedn(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.RSAChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        self.RSAMode = 2
        animation.setEndValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        animation.setDuration(200)
        animation.start()
        self.lableinit()
        self.RSAcBox.setEnabled(True)
        self.RSAdBox.setEnabled(True)
        self.RSAnBox.setEnabled(True)

    def Changedpdqpq(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.RSAChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        self.RSAMode = 3
        animation.setEndValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        animation.setDuration(200)
        animation.start()
        self.lableinit()
        self.RSAcBox.setEnabled(True)
        self.RSAdpBox.setEnabled(True)
        self.RSAdqBox.setEnabled(True)
        self.RSAqBox.setEnabled(True)
        self.RSApBox.setEnabled(True)

    def Changeedpn(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.RSAChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        self.RSAMode = 4
        animation.setEndValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        animation.setDuration(200)
        animation.start()
        self.lableinit()
        self.RSAcBox.setEnabled(True)
        self.RSAdpBox.setEnabled(True)
        self.RSAeBox.setEnabled(True)
        self.RSAnBox.setEnabled(True)

    def Changerabin(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.RSAChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        self.RSAMode = 5
        animation.setEndValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        animation.setDuration(200)
        animation.start()
        self.lableinit()
        self.RSAcBox.setEnabled(True)
        self.RSApBox.setEnabled(True)
        self.RSAqBox.setEnabled(True)
