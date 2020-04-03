from PyQt5 import QtCore, QtWidgets, Qt, QtGui
from CryptoPanel.ui_CryptoPanel import ui_CryptoPanel


class CryptoPanel(ui_CryptoPanel):
    def __init__(self):
        super(CryptoPanel, self).__init__()

        self.BaseButton.clicked.connect(self.ChangeCryptoBase)
        self.QuoteButton.clicked.connect(self.ChangeCryptoQuote)
        self.UrlButton.clicked.connect(self.ChangeCryptoUrl)
        self.HexButton.clicked.connect(self.ChangeCryptoHex)
        self.HTMLButton.clicked.connect(self.ChangeCryptoHTML)
        self.EscapeButton.clicked.connect(self.ChangeCryptoEscape)
        self.TapButton.clicked.connect(self.ChangeCryptoTap)
        self.MorseButton.clicked.connect(self.ChangeCryptoMorse)
        self.HashButton.clicked.connect(self.ChangeCryptoHash)
        self.CaesarButton.clicked.connect(self.ChangeCryptoCaesar)
        self.RailFenceButton.clicked.connect(self.ChangeCryptoRailFence)
        self.ROTButton.clicked.connect(self.ChangeCryptoROT)
        self.StrokesButton.clicked.connect(self.ChangeCryptoStrokes)
        self.RSAButton.clicked.connect(self.ChangeCryptoRSA)

    def ChangeCryptoStrokes(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 44
        self.CryptoStack.setCurrentWidget(self.StrokesPanel)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoROT(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 31
        self.CryptoStack.setCurrentWidget(self.ROTPanel)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoRailFence(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 30
        self.CryptoStack.setCurrentWidget(self.RailFencePanel)
        self.RailFencePanel.RailFenceDivBox.setText('2')
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoCaesar(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 21
        self.CryptoStack.setCurrentWidget(self.CaesarPanel)
        self.CaesarPanel.CaesarLimitBox.setText('26')
        self.CaesarPanel.CaesarStepBox.setText('0')
        self.CaesarPanel.CaesarDispBox.setText('0')
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    # RSA工具

    def ChangeCryptoRSA(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 13
        self.CryptoStack.setCurrentWidget(self.RSAPanel)
        # self.RSAPanel.ChangeRSA()
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()


    def ChangeCryptoHash(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 8
        self.CryptoStack.setCurrentWidget(self.HashPanel)
        self.HashPanel.HashEncodingBox.setText('UTF-8')
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoMorse(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 7
        self.CryptoStack.setCurrentWidget(self.MorsePanel)
        self.MorsePanel.MorseSpiltBox.setText('/')
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoTap(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 6
        self.CryptoStack.setCurrentWidget(self.TapPanel)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoEscape(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 5
        self.CryptoStack.setCurrentWidget(self.EscapePanel)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoHTML(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 4
        self.CryptoStack.setCurrentWidget(self.HTMLPanel)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoHex(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 3
        self.CryptoStack.setCurrentWidget(self.HexPanel)
        self.HexPanel.HexSplitBox.setText('')
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoUrl(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 2
        self.CryptoStack.setCurrentWidget(self.UrlPanel)
        self.UrlPanel.UrlTableBox.setText('utf-8')
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoQuote(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 1
        self.CryptoStack.setCurrentWidget(self.QuotePanel)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoBase(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        self.CryptoMode = 0
        self.CryptoStack.setCurrentWidget(self.BasePanel)
        self.BasePanel.ChangeBase64()
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserVBox[self.CryptoMode % 10], self.CryptoChooserHBox[self.CryptoMode // 10]))
        animation.setDuration(200)
        animation.start()
