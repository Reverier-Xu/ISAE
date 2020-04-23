import copy

from PyQt5 import QtCore, QtWidgets, Qt, QtGui
from DataFlowPanel.ui_DataFlowPanel import ui_CryptoPanel
from ui_Widgets import uni_Widget
from DataFlowPanel.DataFlowNodeBasic import *
from ui_Widgets.qtpynodeeditor import *


class DataFlowPanel(ui_CryptoPanel):
    def __init__(self):
        super(DataFlowPanel, self).__init__()
        self.ToolsSearchBox.textChanged.connect(self.ToolsList.filter)
        self.ToolsList.addDIYItem('Input', '基本')
        self.ToolsList.addDIYItem('Output', '基本')
        self.ToolsList.addDIYItem('Image Output', '基本')
        for i in Modules:
            self.ToolsList.addDIYItem(i, Modules[i].properties['categories'])
        reg = DataModelRegistry()
        reg.register_model(InputModel, category='Basic')
        reg.register_model(OutputModel, category='Basic')
        reg.register_model(ImageShowModel, category='Basic')
        for i in Modules:
            class DIYNodesDataModule(CryptoComputeModel):
                port_caption_visible = True
                data_type = StringData.data_type
                module = Modules[i]
                properties = module.properties
                num_ports = {PortType.input: len(module.properties['input']),
                             PortType.output: len(module.properties['output'])}
                port_caption = {'input': module.properties['input'],
                                'output': module.properties['output']}
                name = Modules[i].properties['name']

                def __init__(self, *args, **kwargs):
                    self.settings = copy(self.module.defaults)
                    self.func = self.module.main
                    self.inputs = {}
                    self.outputs = {}
                    super().__init__(self.module, *args, **kwargs)

            reg.register_model(DIYNodesDataModule, category=Modules[i].properties['categories'])
        scene = FlowScene(reg)
        self.CryptoToolNodeEditor.setScene(scene)
        self.CryptoToolNodeEditor.scene.node_double_clicked.connect(self.OptionsBox.LoadOptions)
        self.SaveOptionsButton.clicked.connect(self.SaveOptionsFunc)

    def SaveOptionsFunc(self):
        try:
            self.OptionsBox.node.model.settings = self.OptionsBox.GetOptions()
        except:
            pass


'''
        self.BaseButton.clicked.connect(self.ChangeCryptoBase)
        self.CryptoNodeButton.clicked.connect(self.ChangeCryptoCryptoNode)
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
        self.ChangeCryptoCryptoNode()

    def ChangeCryptoStrokes(self):
        self.CryptoStack.setCurrentWidget(self.StrokesPanel)
        self.ChangeButtonColor(self.StrokesButton)

    def ChangeCryptoROT(self):
        self.CryptoStack.setCurrentWidget(self.ROTPanel)
        self.ChangeButtonColor(self.ROTButton)

    def ChangeCryptoRailFence(self):
        self.CryptoStack.setCurrentWidget(self.RailFencePanel)
        self.ChangeButtonColor(self.RailFenceButton)

    def ChangeCryptoCaesar(self):
        self.CryptoStack.setCurrentWidget(self.CaesarPanel)
        self.ChangeButtonColor(self.CaesarButton)
        self.CaesarPanel.CaesarLimitBox.setText('26')
        self.CaesarPanel.CaesarStepBox.setText('0')
        self.CaesarPanel.CaesarDispBox.setText('0')

    # RSA工具
    def ChangeCryptoRSA(self):
        self.CryptoStack.setCurrentWidget(self.RSAPanel)
        self.ChangeButtonColor(self.RSAButton)
        # self.RSAPanel.ChangeRSA()

    def ChangeCryptoHash(self):
        self.CryptoStack.setCurrentWidget(self.HashPanel)
        self.ChangeButtonColor(self.HashButton)
        self.HashPanel.HashEncodingBox.setText('UTF-8')

    def ChangeCryptoMorse(self):
        self.CryptoStack.setCurrentWidget(self.MorsePanel)
        self.ChangeButtonColor(self.MorseButton)
        self.MorsePanel.MorseSpiltBox.setText('/')

    def ChangeCryptoTap(self):
        self.CryptoStack.setCurrentWidget(self.TapPanel)
        self.ChangeButtonColor(self.TapButton)

    def ChangeCryptoEscape(self):
        self.CryptoStack.setCurrentWidget(self.EscapePanel)
        self.ChangeButtonColor(self.EscapeButton)

    def ChangeCryptoHTML(self):
        self.CryptoStack.setCurrentWidget(self.HTMLPanel)
        self.ChangeButtonColor(self.HTMLButton)

    def ChangeCryptoHex(self):
        self.CryptoStack.setCurrentWidget(self.HexPanel)
        self.ChangeButtonColor(self.HexButton)
        self.HexPanel.HexSplitBox.setText('')

    def ChangeCryptoUrl(self):
        self.CryptoStack.setCurrentWidget(self.UrlPanel)
        self.ChangeButtonColor(self.UrlButton)
        self.UrlPanel.UrlTableBox.setText('utf-8')

    def ChangeCryptoQuote(self):
        self.CryptoStack.setCurrentWidget(self.QuotePanel)
        self.ChangeButtonColor(self.QuoteButton)

    def ChangeCryptoBase(self):
        self.CryptoStack.setCurrentWidget(self.BasePanel)
        self.ChangeButtonColor(self.BaseButton)
        self.BasePanel.ChangeBase64()

    def ChangeCryptoCryptoNode(self):
        self.CryptoStack.setCurrentWidget(self.CryptoNodePanel)
        self.ChangeButtonColor(self.CryptoNodeButton)

    def ChangeButtonColor(self, button):
        self.CryptoNodeButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.BaseButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.QuoteButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.UrlButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.HexButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.HTMLButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.EscapeButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.TapButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.MorseButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.HashButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.AESButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.DESButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.RC4Button.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.ASCIITranslateButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.RSAButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.CodeTranslateButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.ADFGVXButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.AffineButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.AutoKeyButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.AtbashButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.BeaufortButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.BifidButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.CaesarButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.CTButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.EnigmaButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.FourSquareButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.GronsFeldButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.M209Button.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.PlayFairButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.PolybiusButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.PortaButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.RailFenceButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.ROTButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.SubstitutionButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.VigenereButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.PigenButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.BaconButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.RunningKeyButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.HillButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.A1z26Button.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.BeaufortButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.OtherCipherButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.JSFuckButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.BrainFuckButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.OokButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.StrokesButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        button.setStyleSheet(uni_Widget.ButtonStyleSelected)
'''
