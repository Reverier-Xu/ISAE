from PyQt5 import QtCore, QtWidgets, QtGui
from ui_Widgets import uni_Widget
from CryptoPanel.BaseModule.BaseModule import BasePanel
from CryptoPanel.QuoteModule.QuoteModule import QuotePanel
from CryptoPanel.UrlModule.UrlModule import UrlPanel
from CryptoPanel.HexModule.HexModule import HexPanel
from CryptoPanel.HTMLModule.HTMLModule import HTMLPanel
from CryptoPanel.EscapeModule.EscapeModule import EscapePanel
from CryptoPanel.TapModule.TapModule import TapPanel
from CryptoPanel.MorseModule.MorseModule import MorsePanel
from CryptoPanel.HashModule.HashModule import HashPanel
from CryptoPanel.CaesarModule.CaesarModule import CaesarPanel
from CryptoPanel.RailFenceModule.RailFenceModule import RailFencePanel
from CryptoPanel.PawnshopModule.PawnshopModule import PawnshopPanel


class ui_CryptoPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_CryptoPanel, self).__init__()
        # Crypto Buttons

        self.CryptoMode = 0
        self.CryptoChoosePanel = QtWidgets.QWidget()
        self.CryptoChoosePanel.setObjectName('CryptoChoosePanel')
        self.CryptoChoosePanel.setStyleSheet('#CryptoChoosePanel{background-color: transparent}')
        self.CryptoChoosePanel.setGeometry(0, 0, 1420, 300)

        self.CryptoChoosePanelScroll = uni_Widget.ICTFEScrollArea(self)
        self.CryptoChoosePanelScroll.setGeometry(0, 0, 1426, 128)
        self.CryptoChoosePanelScroll.setWidget(self.CryptoChoosePanel)

        # Base Button
        self.BaseButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.BaseButton.setGeometry(QtCore.QRect(11, 10, 120, 45))
        self.BaseButton.setText("Base系列")
        self.BaseButton.setObjectName("BaseButton")

        # Quote-Printable Button
        self.QuoteButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.QuoteButton.setGeometry(QtCore.QRect(141, 10, 120, 45))
        self.QuoteButton.setText("Quote-P")
        self.QuoteButton.setObjectName("QuoteButton")

        # Url Button
        self.UrlButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.UrlButton.setGeometry(QtCore.QRect(271, 10, 120, 45))
        self.UrlButton.setText("Url编码")
        self.UrlButton.setObjectName("UrlButton")

        # Hex Button
        self.HexButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.HexButton.setGeometry(QtCore.QRect(401, 10, 120, 45))
        self.HexButton.setText("Hex编码")
        self.HexButton.setObjectName("HexButton")

        # HTML Button
        self.HTMLButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.HTMLButton.setGeometry(QtCore.QRect(531, 10, 120, 45))
        self.HTMLButton.setText("HTML编码")
        self.HTMLButton.setObjectName("HTMLButton")

        # Escape Button
        self.EscapeButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.EscapeButton.setGeometry(QtCore.QRect(661, 10, 120, 45))
        self.EscapeButton.setText("Escape")
        self.EscapeButton.setObjectName("EscapeButton")

        # Tap Button
        self.TapButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.TapButton.setGeometry(QtCore.QRect(791, 10, 120, 45))
        self.TapButton.setText("敲击码")
        self.TapButton.setObjectName("TapButton")

        # Morse Button
        self.MorseButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.MorseButton.setGeometry(QtCore.QRect(921, 10, 120, 45))
        self.MorseButton.setText("摩斯电码")
        self.MorseButton.setObjectName("MorseButton")

        # Hash Button
        self.HashButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.HashButton.setGeometry(QtCore.QRect(1051, 10, 120, 45))
        self.HashButton.setText("Hash计算")
        self.HashButton.setObjectName("HashButton")

        # AES Button
        self.AESButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.AESButton.setGeometry(QtCore.QRect(1181, 10, 120, 45))
        self.AESButton.setText("AES加密")
        self.AESButton.setObjectName("AESButton")

        # DES Button
        self.DESButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.DESButton.setGeometry(QtCore.QRect(11, 65, 120, 45))
        self.DESButton.setText("DES加密")
        self.DESButton.setObjectName("DESButton")

        # RC4 Button
        self.RC4Button = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.RC4Button.setGeometry(QtCore.QRect(141, 65, 120, 45))
        self.RC4Button.setText("RC4编码")
        self.RC4Button.setObjectName("RC4Button")

        # ASCIITranslate Button
        self.ASCIITranslateButton = uni_Widget.ICTFEButton(
            self.CryptoChoosePanel)
        self.ASCIITranslateButton.setGeometry(QtCore.QRect(271, 65, 120, 45))
        self.ASCIITranslateButton.setText("进制转换")
        self.ASCIITranslateButton.setObjectName("ASCIITranslateButton")

        # RSA Button
        self.RSAButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.RSAButton.setGeometry(QtCore.QRect(401, 65, 120, 45))
        self.RSAButton.setText("RSA工具")
        self.RSAButton.setObjectName("RSAButton")

        # CodeTranslate Button
        self.CodeTranslateButton = uni_Widget.ICTFEButton(
            self.CryptoChoosePanel)
        self.CodeTranslateButton.setGeometry(QtCore.QRect(531, 65, 120, 45))
        self.CodeTranslateButton.setText("编码转换")
        self.CodeTranslateButton.setObjectName("CodeTranslateButton")

        # ADFGVX Button
        self.ADFGVXButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.ADFGVXButton.setGeometry(QtCore.QRect(661, 65, 120, 45))
        self.ADFGVXButton.setText("ADFGVX")
        self.ADFGVXButton.setObjectName("ADFGVXButton")

        # Affine Button
        self.AffineButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.AffineButton.setGeometry(QtCore.QRect(791, 65, 120, 45))
        self.AffineButton.setText("仿射密码")
        self.AffineButton.setObjectName("AffineButton")

        # AutoKey Button
        self.AutoKeyButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.AutoKeyButton.setGeometry(QtCore.QRect(921, 65, 120, 45))
        self.AutoKeyButton.setText("自动密钥机")
        self.AutoKeyButton.setObjectName("AutoKeyButton")

        # Atbash Button
        self.AtbashButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.AtbashButton.setGeometry(QtCore.QRect(1051, 65, 120, 45))
        self.AtbashButton.setText("Atbash")
        self.AtbashButton.setObjectName("AtbashButton")

        # Beaufort Button
        self.BeaufortButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.BeaufortButton.setGeometry(QtCore.QRect(1181, 65, 120, 45))
        self.BeaufortButton.setText("Beaufort")
        self.BeaufortButton.setObjectName("BeaufortButton")

        # Bifid Button
        self.BifidButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.BifidButton.setGeometry(QtCore.QRect(11, 120, 120, 45))
        self.BifidButton.setText("Bifid")
        self.BifidButton.setObjectName("BifidButton")

        # Caesar Button
        self.CaesarButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.CaesarButton.setGeometry(QtCore.QRect(141, 120, 120, 45))
        self.CaesarButton.setText("Caesar")
        self.CaesarButton.setObjectName("CaesarButton")

        # CT Button
        self.CTButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.CTButton.setGeometry(QtCore.QRect(271, 120, 120, 45))
        self.CTButton.setText("列移位")
        self.CTButton.setObjectName("CTButton")

        # Enigma Button
        self.EnigmaButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.EnigmaButton.setGeometry(QtCore.QRect(401, 120, 120, 45))
        self.EnigmaButton.setText("Enigma")
        self.EnigmaButton.setObjectName("EnigmaButton")

        # FourSquare Button
        self.FourSquareButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.FourSquareButton.setGeometry(QtCore.QRect(531, 120, 120, 45))
        self.FourSquareButton.setText("四方密码")
        self.FourSquareButton.setObjectName("FourSquareButton")

        # GronsFeld Button
        self.GronsFeldButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.GronsFeldButton.setGeometry(QtCore.QRect(661, 120, 120, 45))
        self.GronsFeldButton.setText("GronsFeld")
        self.GronsFeldButton.setObjectName("GronsFeldButton")

        # M209 Button
        self.M209Button = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.M209Button.setGeometry(QtCore.QRect(791, 120, 120, 45))
        self.M209Button.setText("M-209")
        self.M209Button.setObjectName("M209Button")

        # PlayFair Button
        self.PlayFairButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.PlayFairButton.setGeometry(QtCore.QRect(921, 120, 120, 45))
        self.PlayFairButton.setText("PlayFair")
        self.PlayFairButton.setObjectName("PlayFairButton")

        # Polybius Button
        self.PolybiusButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.PolybiusButton.setGeometry(QtCore.QRect(1051, 120, 120, 45))
        self.PolybiusButton.setText("Polybius")
        self.PolybiusButton.setObjectName("PolybiusButton")

        # Porta Button
        self.PortaButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.PortaButton.setGeometry(QtCore.QRect(1181, 120, 120, 45))
        self.PortaButton.setText("Porta")
        self.PortaButton.setObjectName("PortaButton")

        # Railfence Button
        self.RailFenceButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.RailFenceButton.setGeometry(QtCore.QRect(11, 175, 120, 45))
        self.RailFenceButton.setText("栅栏密码")
        self.RailFenceButton.setObjectName("RailFenceButton")

        # Rot13 Button
        self.Rot13Button = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.Rot13Button.setGeometry(QtCore.QRect(141, 175, 120, 45))
        self.Rot13Button.setText("Rot13")
        self.Rot13Button.setObjectName("Rot13Button")

        # Substitution Button
        self.SubstitutionButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.SubstitutionButton.setGeometry(QtCore.QRect(271, 175, 120, 45))
        self.SubstitutionButton.setText("简单换位")
        self.SubstitutionButton.setObjectName("SubstitutionButton")

        # Vigenere Button
        self.VigenereButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.VigenereButton.setGeometry(QtCore.QRect(401, 175, 120, 45))
        self.VigenereButton.setText("Vigenere")
        self.VigenereButton.setObjectName("VigenereButton")

        # Pigen Button
        self.PigenButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.PigenButton.setGeometry(QtCore.QRect(531, 175, 120, 45))
        self.PigenButton.setText("猪圈密码")
        self.PigenButton.setObjectName("PigenButton")

        # Bacon Button
        self.BaconButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.BaconButton.setGeometry(QtCore.QRect(661, 175, 120, 45))
        self.BaconButton.setText("培根密码")
        self.BaconButton.setObjectName("BaconButton")

        # RunningKey Button
        self.RunningKeyButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.RunningKeyButton.setGeometry(QtCore.QRect(791, 175, 120, 45))
        self.RunningKeyButton.setText("滚动密钥")
        self.RunningKeyButton.setObjectName("RunningKeyButton")

        # Hill Button
        self.HillButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.HillButton.setGeometry(QtCore.QRect(921, 175, 120, 45))
        self.HillButton.setText("希尔密码")
        self.HillButton.setObjectName("HillButton")

        # A1z26 Button
        self.A1z26Button = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.A1z26Button.setGeometry(QtCore.QRect(1051, 175, 120, 45))
        self.A1z26Button.setText("A1z26")
        self.A1z26Button.setObjectName("A1z26Button")

        # Beaufort Button
        self.BeaufortButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.BeaufortButton.setGeometry(QtCore.QRect(1181, 175, 120, 45))
        self.BeaufortButton.setText("Beaufort")
        self.BeaufortButton.setObjectName("BeaufortButton")

        # OtherCipher Button
        self.OtherCipherButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.OtherCipherButton.setGeometry(QtCore.QRect(11, 230, 120, 45))
        self.OtherCipherButton.setText("编码杂项")
        self.OtherCipherButton.setObjectName("OtherCipherButton")

        # JSFuck Button
        self.JSFuckButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.JSFuckButton.setGeometry(QtCore.QRect(141, 230, 120, 45))
        self.JSFuckButton.setText("JSFuck")
        self.JSFuckButton.setObjectName("JSFuckButton")

        # BrainFuck Button
        self.BrainFuckButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.BrainFuckButton.setGeometry(QtCore.QRect(271, 230, 120, 45))
        self.BrainFuckButton.setText("BrainFuck")
        self.BrainFuckButton.setObjectName("BrainFuckButton")

        # Ook Button
        self.OokButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.OokButton.setGeometry(QtCore.QRect(401, 230, 120, 45))
        self.OokButton.setText("Ook!")
        self.OokButton.setObjectName("OokButton")

        # Pawnshop Button
        self.PawnshopButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.PawnshopButton.setGeometry(QtCore.QRect(531, 230, 120, 45))
        self.PawnshopButton.setText("当铺密码")
        self.PawnshopButton.setObjectName("PawnshopButton")

        # end Crypto Buttons

        # Choose ticker
        self.CryptoChooserVBox = [11, 141, 271, 401, 531, 661, 791, 921, 1051, 1181]
        self.CryptoChooserHBox = [55, 110, 165, 220, 275]
        self.CryptoChooser = QtWidgets.QLabel(self.CryptoChoosePanel)
        self.CryptoChooser.setPixmap(
            QtGui.QPixmap('./Resources/chooser.png'))
        self.CryptoChooser.setGeometry(QtCore.QRect(
            self.CryptoChooserVBox[self.CryptoMode], 55, 120, 8))

        # Crypto Panel change methods
        self.CryptoStack = QtWidgets.QStackedWidget(self)
        self.CryptoStack.setGeometry(QtCore.QRect(1, 135, 1423, 613))
        self.CryptoStack.setObjectName('CryptoStack')

        # Base panel
        self.BasePanel = BasePanel()
        self.BasePanel.setObjectName('BasePanel')
        self.CryptoStack.addWidget(self.BasePanel)

        # Quote panel
        self.QuotePanel = QuotePanel()
        self.QuotePanel.setObjectName('QuotePanel')
        self.CryptoStack.addWidget(self.QuotePanel)

        # Url panel
        self.UrlPanel = UrlPanel()
        self.UrlPanel.setObjectName('UrlPanel')
        self.CryptoStack.addWidget(self.UrlPanel)

        # Hex panel
        self.HexPanel = HexPanel()
        self.HexPanel.setObjectName('HexPanel')
        self.CryptoStack.addWidget(self.HexPanel)

        # HTML panel
        self.HTMLPanel = HTMLPanel()
        self.HTMLPanel.setObjectName('HTMLPanel')
        self.CryptoStack.addWidget(self.HTMLPanel)

        # Escape panel
        self.EscapePanel = EscapePanel()
        self.EscapePanel.setObjectName('EscapePanel')
        self.CryptoStack.addWidget(self.EscapePanel)

        # Tap panel
        self.TapPanel = TapPanel()
        self.TapPanel.setObjectName('TapPanel')
        self.CryptoStack.addWidget(self.TapPanel)

        # Morse panel
        self.MorsePanel = MorsePanel()
        self.MorsePanel.setObjectName('MorsePanel')
        self.CryptoStack.addWidget(self.MorsePanel)

        # Hash panel
        self.HashPanel = HashPanel()
        self.HashPanel.setObjectName('HashPanel')
        self.CryptoStack.addWidget(self.HashPanel)

        # Caesar panel
        self.CaesarPanel = CaesarPanel()
        self.CaesarPanel.setObjectName('CaesarPanel')
        self.CryptoStack.addWidget(self.CaesarPanel)

        # RailFence panel
        self.RailFencePanel = RailFencePanel()
        self.RailFencePanel.setObjectName('RailFencePanel')
        self.CryptoStack.addWidget(self.RailFencePanel)

        # Pawnshop panel
        self.PawnshopPanel = PawnshopPanel()
        self.PawnshopPanel.setObjectName('PawnshopPanel')
        self.CryptoStack.addWidget(self.PawnshopPanel)
