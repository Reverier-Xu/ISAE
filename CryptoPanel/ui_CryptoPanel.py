from PyQt5 import QtCore, QtWidgets, QtGui
from ui_Widgets import uni_Widget
from ui_Widgets.qtpynodeeditor import *
from CryptoPanel.CryptoNodeBasic import *

'''
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
from CryptoPanel.StrokesModule.StrokesModule import StrokesPanel
from CryptoPanel.ROTModule.ROTModule import ROTPanel
from CryptoPanel.RSAModule.RSAModule import RSAPanel
'''


class ui_CryptoPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_CryptoPanel, self).__init__()
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CryptoMainSpliter = uni_Widget.ICTFESplitter(self)

        self.CryptoMainSpliter.setOrientation(QtCore.Qt.Horizontal)
        self.CryptoMainSpliter.setObjectName("CryptoMainSpliter")
        self.ToolsArea = uni_Widget.ICTFEScrollArea(self.CryptoMainSpliter)
        self.ToolsArea.setWidgetResizable(True)
        self.ToolsArea.setObjectName("ToolsArea")
        self.ToolsAreaPanel = QtWidgets.QWidget()
        self.ToolsAreaPanel.setGeometry(QtCore.QRect(0, 0, 386, 698))
        self.ToolsAreaPanel.setObjectName("ToolsAreaPanel")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.ToolsAreaPanel)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ToolsSearchBox = QtWidgets.QLineEdit(self.ToolsAreaPanel)
        self.ToolsSearchBox.setStyleSheet('color: white;'
                                          'border: 1px solid gray;'
                                          'border-radius: 5px;'
                                          'padding: 5px;'
                                          'background: rgb(20, 20, 20);'
                                          'selection-background-color: blue;')
        self.ToolsSearchBox.setPlaceholderText('搜索...')
        self.ToolsSearchBox.setObjectName("ToolsSearchBox")
        self.verticalLayout_5.addWidget(self.ToolsSearchBox)
        self.ToolsList = DragList(self.ToolsAreaPanel)
        self.ToolsList.setStyleSheet('background-color: transparent; border: 1px solid grey;')
        self.ToolsList.setObjectName("ToolsList")
        self.verticalLayout_5.addWidget(self.ToolsList)
        self.ToolsArea.setWidget(self.ToolsAreaPanel)
        self.widget = QtWidgets.QWidget(self.CryptoMainSpliter)
        self.widget.setObjectName("widget")
        self.NodeEditorLayout = QtWidgets.QVBoxLayout(self.widget)
        self.NodeEditorLayout.setContentsMargins(0, 0, 0, 0)
        self.NodeEditorLayout.setObjectName("NodeEditorLayout")
        self.NodeEditorLayout.setSpacing(0)
        scene = FlowScene()
        self.CryptoToolNodeEditor = CryptoFlowView(scene)
        self.CryptoToolNodeEditor.setMinimumWidth(1000)
        self.CryptoToolNodeEditor.setObjectName("CryptoToolNodeEditor")
        self.NodeEditorLayout.addWidget(self.CryptoToolNodeEditor)
        self.NodeEditorLayout.addWidget(self.CryptoToolNodeEditor)
        self.FileAndOptionsLayout = uni_Widget.ICTFESplitter(self.CryptoMainSpliter)
        self.FileAndOptionsLayout.setOrientation(QtCore.Qt.Vertical)
        self.FileAndOptionsLayout.setObjectName("FileAndOptionsLayout")
        self.OptionsArea = uni_Widget.ICTFEScrollArea(self.FileAndOptionsLayout)
        self.OptionsArea.setWidgetResizable(True)
        self.OptionsArea.setObjectName("OptionsArea")
        self.OptionsAreaPanel = QtWidgets.QWidget()
        self.OptionsAreaPanel.setGeometry(QtCore.QRect(0, 0, 386, 348))
        self.OptionsAreaPanel.setObjectName("OptionsAreaPanel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.OptionsAreaPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.OptionsTips = uni_Widget.ICTFELabel(self.OptionsAreaPanel)
        self.OptionsTips.setObjectName("OptionsTips")
        self.verticalLayout.addWidget(self.OptionsTips)
        self.OptionsBox = uni_Widget.ICTFEList(self.OptionsAreaPanel)
        self.OptionsBox.setObjectName("OptionsBox")
        self.verticalLayout.addWidget(self.OptionsBox)
        self.OptionsArea.setWidget(self.OptionsAreaPanel)
        self.FileTempStackArea = uni_Widget.ICTFEScrollArea(self.FileAndOptionsLayout)
        self.FileTempStackArea.setWidgetResizable(True)
        self.FileTempStackArea.setObjectName("FileTempStackArea")
        self.FileTempStackAreaPanel = QtWidgets.QWidget()
        self.FileTempStackAreaPanel.setGeometry(QtCore.QRect(0, 0, 386, 347))
        self.FileTempStackAreaPanel.setObjectName("FileTempStackAreaPanel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.FileTempStackAreaPanel)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FileTempStackTips = uni_Widget.ICTFELabel(self.FileTempStackAreaPanel)
        self.FileTempStackTips.setObjectName("FileTempStackTips")
        self.verticalLayout_2.addWidget(self.FileTempStackTips)
        self.FileTempStack = uni_Widget.ICTFEList(self.FileTempStackAreaPanel)
        self.FileTempStack.setObjectName("FileTempStack")
        self.verticalLayout_2.addWidget(self.FileTempStack)
        self.FileTempStackArea.setWidget(self.FileTempStackAreaPanel)
        self.horizontalLayout_2.addWidget(self.CryptoMainSpliter)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.OptionsTips.setText(_translate("self", "节点选项"))
        self.FileTempStackTips.setText(_translate("self", "暂存池"))


'''
        # Crypto Buttons
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.CryptoChoosePanelScroll = uni_Widget.ICTFEScrollArea(self)
        sizePolicy.setHeightForWidth(
            self.CryptoChoosePanelScroll.sizePolicy().hasHeightForWidth())
        self.Layouts = QtWidgets.QHBoxLayout(self)
        self.Layouts.setObjectName('Layouts')
        self.Layouts.setSpacing(10)
        self.Layouts.setContentsMargins(10, 15, 10, 15)
        self.CryptoChoosePanel = QtWidgets.QWidget()
        self.CryptoChoosePanel.setObjectName('CryptoChoosePanel')
        self.CryptoChoosePanel.setStyleSheet(
            '#CryptoChoosePanel{background-color: transparent}')
        self.CryptoChoosePanel.setGeometry(QtCore.QRect(0, 0, 1420, 300))

        self.CryptoChoosePanelScroll.setGeometry(QtCore.QRect(0, 0, 128, 900))
        self.CryptoChoosePanelScroll.setMinimumWidth(128)
        self.CryptoChoosePanelScroll.setWidget(self.CryptoChoosePanel)
        self.CryptoChoosePanelScroll.setSizePolicy(sizePolicy)
        self.CryptoChoosePanelScroll.setWidgetResizable(True)
        self.CryptoChoosePanelScroll.setObjectName('CryptoChoosePanelScroll')

        self.Layouts.addWidget(self.CryptoChoosePanelScroll)

        self.buttonLayout = QtWidgets.QVBoxLayout()
        self.buttonLayout.setSpacing(5)

        # Crypto Node Button
        self.CryptoNodeButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.CryptoNodeButton.setText("数据流")
        self.CryptoNodeButton.setObjectName("CryptoNodeButton")
        self.buttonLayout.addWidget(self.CryptoNodeButton)

        # CryptoNode Button
        self.BaseButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.BaseButton.setText("Base系列")
        self.BaseButton.setObjectName("BaseButton")
        self.buttonLayout.addWidget(self.BaseButton)

        # Quote-Printable Button
        self.QuoteButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.QuoteButton)
        self.QuoteButton.setText("Quote-P")
        self.QuoteButton.setObjectName("QuoteButton")

        # Url Button
        self.UrlButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.UrlButton)
        self.UrlButton.setText("Url编码")
        self.UrlButton.setObjectName("UrlButton")

        # Hex Button
        self.HexButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.HexButton)
        self.HexButton.setText("Hex编码")
        self.HexButton.setObjectName("HexButton")

        # HTML Button
        self.HTMLButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.HTMLButton)
        self.HTMLButton.setText("HTML编码")
        self.HTMLButton.setObjectName("HTMLButton")

        # Escape Button
        self.EscapeButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.EscapeButton)
        self.EscapeButton.setText("Escape")
        self.EscapeButton.setObjectName("EscapeButton")

        # Tap Button
        self.TapButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.TapButton)
        self.TapButton.setText("敲击码")
        self.TapButton.setObjectName("TapButton")

        # Morse Button
        self.MorseButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.MorseButton)
        self.MorseButton.setText("摩斯电码")
        self.MorseButton.setObjectName("MorseButton")

        # Hash Button
        self.HashButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.HashButton)
        self.HashButton.setText("Hash计算")
        self.HashButton.setObjectName("HashButton")

        # AES Button
        self.AESButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.AESButton)
        self.AESButton.setText("AES加密")
        self.AESButton.setObjectName("AESButton")

        # DES Button
        self.DESButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.DESButton)
        self.DESButton.setText("DES加密")
        self.DESButton.setObjectName("DESButton")

        # RC4 Button
        self.RC4Button = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.RC4Button)
        self.RC4Button.setText("RC4编码")
        self.RC4Button.setObjectName("RC4Button")

        # ASCIITranslate Button
        self.ASCIITranslateButton = uni_Widget.ICTFEButton(
            self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.ASCIITranslateButton)
        self.ASCIITranslateButton.setText("进制转换")
        self.ASCIITranslateButton.setObjectName("ASCIITranslateButton")

        # RSA Button
        self.RSAButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.RSAButton)
        self.RSAButton.setText("RSA工具")
        self.RSAButton.setObjectName("RSAButton")

        # CodeTranslate Button
        self.CodeTranslateButton = uni_Widget.ICTFEButton(
            self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.CodeTranslateButton)
        self.CodeTranslateButton.setText("编码转换")
        self.CodeTranslateButton.setObjectName("CodeTranslateButton")

        # ADFGVX Button
        self.ADFGVXButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.ADFGVXButton)
        self.ADFGVXButton.setText("ADFGVX")
        self.ADFGVXButton.setObjectName("ADFGVXButton")

        # Affine Button
        self.AffineButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.AffineButton)
        self.AffineButton.setText("仿射密码")
        self.AffineButton.setObjectName("AffineButton")

        # AutoKey Button
        self.AutoKeyButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.AutoKeyButton)
        self.AutoKeyButton.setText("自动密钥机")
        self.AutoKeyButton.setObjectName("AutoKeyButton")

        # Atbash Button
        self.AtbashButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.AtbashButton)
        self.AtbashButton.setText("Atbash")
        self.AtbashButton.setObjectName("AtbashButton")

        # Beaufort Button
        self.BeaufortButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.BeaufortButton)
        self.BeaufortButton.setText("Beaufort")
        self.BeaufortButton.setObjectName("BeaufortButton")

        # Bifid Button
        self.BifidButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.BifidButton)
        self.BifidButton.setText("Bifid")
        self.BifidButton.setObjectName("BifidButton")

        # Caesar Button
        self.CaesarButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.CaesarButton)
        self.CaesarButton.setText("Caesar")
        self.CaesarButton.setObjectName("CaesarButton")

        # CT Button
        self.CTButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.CTButton)
        self.CTButton.setText("列移位")
        self.CTButton.setObjectName("CTButton")

        # Enigma Button
        self.EnigmaButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.EnigmaButton)
        self.EnigmaButton.setText("Enigma")
        self.EnigmaButton.setObjectName("EnigmaButton")

        # FourSquare Button
        self.FourSquareButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.FourSquareButton)
        self.FourSquareButton.setText("四方密码")
        self.FourSquareButton.setObjectName("FourSquareButton")

        # GronsFeld Button
        self.GronsFeldButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.GronsFeldButton)
        self.GronsFeldButton.setText("GronsFeld")
        self.GronsFeldButton.setObjectName("GronsFeldButton")

        # M209 Button
        self.M209Button = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.M209Button)
        self.M209Button.setText("M-209")
        self.M209Button.setObjectName("M209Button")

        # PlayFair Button
        self.PlayFairButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.PlayFairButton)
        self.PlayFairButton.setText("PlayFair")
        self.PlayFairButton.setObjectName("PlayFairButton")

        # Polybius Button
        self.PolybiusButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.PolybiusButton)
        self.PolybiusButton.setText("Polybius")
        self.PolybiusButton.setObjectName("PolybiusButton")

        # Porta Button
        self.PortaButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.PortaButton)
        self.PortaButton.setText("Porta")
        self.PortaButton.setObjectName("PortaButton")

        # Railfence Button
        self.RailFenceButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.RailFenceButton)
        self.RailFenceButton.setText("栅栏密码")
        self.RailFenceButton.setObjectName("RailFenceButton")

        # Rot Button
        self.ROTButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.ROTButton)
        self.ROTButton.setText("R O T")
        self.ROTButton.setObjectName("ROTButton")

        # Substitution Button
        self.SubstitutionButton = uni_Widget.ICTFEButton(
            self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.SubstitutionButton)
        self.SubstitutionButton.setText("简单换位")
        self.SubstitutionButton.setObjectName("SubstitutionButton")

        # Vigenere Button
        self.VigenereButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.VigenereButton)
        self.VigenereButton.setText("Vigenere")
        self.VigenereButton.setObjectName("VigenereButton")

        # Pigen Button
        self.PigenButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.PigenButton)
        self.PigenButton.setText("猪圈密码")
        self.PigenButton.setObjectName("PigenButton")

        # Bacon Button
        self.BaconButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.BaconButton)
        self.BaconButton.setText("培根密码")
        self.BaconButton.setObjectName("BaconButton")

        # RunningKey Button
        self.RunningKeyButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.RunningKeyButton)
        self.RunningKeyButton.setText("滚动密钥")
        self.RunningKeyButton.setObjectName("RunningKeyButton")

        # Hill Button
        self.HillButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.HillButton)
        self.HillButton.setText("希尔密码")
        self.HillButton.setObjectName("HillButton")

        # A1z26 Button
        self.A1z26Button = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.A1z26Button)
        self.A1z26Button.setText("A1z26")
        self.A1z26Button.setObjectName("A1z26Button")

        # Beaufort Button
        self.BeaufortButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.BeaufortButton)
        self.BeaufortButton.setText("Beaufort")
        self.BeaufortButton.setObjectName("BeaufortButton")

        # OtherCipher Button
        self.OtherCipherButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.OtherCipherButton)
        self.OtherCipherButton.setText("编码杂项")
        self.OtherCipherButton.setObjectName("OtherCipherButton")

        # JSFuck Button
        self.JSFuckButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.JSFuckButton)
        self.JSFuckButton.setText("JSFuck")
        self.JSFuckButton.setObjectName("JSFuckButton")

        # BrainFuck Button
        self.BrainFuckButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.BrainFuckButton)
        self.BrainFuckButton.setText("BrainFuck")
        self.BrainFuckButton.setObjectName("BrainFuckButton")

        # Ook Button
        self.OokButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.OokButton)
        self.OokButton.setText("Ook!")
        self.OokButton.setObjectName("OokButton")

        # Strokes Button
        self.StrokesButton = uni_Widget.ICTFEButton(self.CryptoChoosePanel)
        self.buttonLayout.addWidget(self.StrokesButton)
        self.StrokesButton.setText("笔画密码")
        self.StrokesButton.setObjectName("StrokesButton")

        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setSpacing(15)

        self.CryptoChoosePanel.setLayout(self.buttonLayout)
        self.CryptoChoosePanel.setGeometry(QtCore.QRect(130, 2875, 0, 0))

        # end Crypto Buttons

        # Crypto Panel change methods
        self.CryptoStack = QtWidgets.QStackedWidget(self)
        self.CryptoStack.setObjectName('CryptoStack')
        self.CryptoStack.setStyleSheet(
            'QWidget{border-style: inset;border: 1px grey;}')

        self.SplitterWidget1 = QtWidgets.QWidget(self)
        self.SplitterWidget1.setMaximumWidth(1)
        self.SplitterWidget1.setMinimumWidth(1)
        self.SplitterWidget1.setStyleSheet("QWidget{\n"
                                           "background-color: grey;\n"
                                           "border: 1px grey;\n"
                                           "border-style: solid;\n"
                                           "}")
        self.Layouts.addWidget(self.SplitterWidget1)

        self.Layouts.addWidget(self.CryptoStack)

        # Base panel
        self.BasePanel = BasePanel()
        self.BasePanel.setObjectName('BasePanel')
        self.CryptoStack.addWidget(self.BasePanel)

        # CryptoNode panel
        self.scene = nodeeditor.FlowScene()
        self.CryptoNodePanel = nodeeditor.FlowView(self.scene)
        self.CryptoNodePanel.setObjectName('CryptoNodePanel')
        self.CryptoStack.addWidget(self.CryptoNodePanel)

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

        # ROT panel
        self.ROTPanel = ROTPanel()
        self.ROTPanel.setObjectName('ROTPanel')
        self.CryptoStack.addWidget(self.ROTPanel)

        # Strokes panel
        self.StrokesPanel = StrokesPanel()
        self.StrokesPanel.setObjectName('StrokesPanel')
        self.CryptoStack.addWidget(self.StrokesPanel)

        # RSA panel
        self.RSAPanel = RSAPanel()
        self.RSAPanel.setObjectName('RSAPanel')
        self.CryptoStack.addWidget(self.RSAPanel)

        self.Layouts.addWidget(self.CryptoStack)
        self.setLayout(self.Layouts)
'''
