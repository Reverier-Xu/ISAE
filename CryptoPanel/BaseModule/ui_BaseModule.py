from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Widgets import uni_Widget


class ui_BasePanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_BasePanel, self).__init__()
        self.BaseMode = 1
        
        self.BaseChooserBox = [0, 10, 140, 270, 400, 530]
        self.BaseChooser = QtWidgets.QLabel(self)
        self.BaseChooser.setPixmap(
            QtGui.QPixmap('./Resources/chooser.png'))
        self.BaseChooser.setGeometry(QtCore.QRect(
            self.BaseChooserBox[self.BaseMode], 55, 120, 8))

        # Base change Buttons
        self.Base64Button = uni_Widget.ICTFEButton(self)
        self.Base64Button.setObjectName('Base64Button')
        self.Base64Button.setGeometry(QtCore.QRect(10, 10, 120, 45))
        self.Base64Button.setText('Base64')

        self.Base32Button = uni_Widget.ICTFEButton(self)
        self.Base32Button.setObjectName('Base32Button')
        self.Base32Button.setGeometry(QtCore.QRect(140, 10, 120, 45))
        self.Base32Button.setText('Base32')

        self.Base16Button = uni_Widget.ICTFEButton(self)
        self.Base16Button.setObjectName('Base16Button')
        self.Base16Button.setGeometry(QtCore.QRect(270, 10, 120, 45))
        self.Base16Button.setText('Base16')

        self.Base85Button = uni_Widget.ICTFEButton(self)
        self.Base85Button.setObjectName('Base85Button')
        self.Base85Button.setGeometry(QtCore.QRect(400, 10, 120, 45))
        self.Base85Button.setText('Base85ASC')

        self.Base85RFCButton = uni_Widget.ICTFEButton(self)
        self.Base85RFCButton.setObjectName('Base85RFCButton')
        self.Base85RFCButton.setGeometry(QtCore.QRect(530, 10, 120, 45))
        self.Base85RFCButton.setText('Base85RFC')

        self.BaseEButton = uni_Widget.ICTFEButton(self)
        self.BaseEButton.setObjectName('BaseEButton')
        self.BaseEButton.setGeometry(QtCore.QRect(1180, 10, 200, 45))
        self.BaseEButton.setText('Base64隐写提取')

        # end base change buttons

        # eval support
        self.BaseTextEvalCheckBox = uni_Widget.ICTFECheckBox(self)
        self.BaseTextEvalCheckBox.setGeometry(QtCore.QRect(540, 135, 120, 40))
        self.BaseTextEvalCheckBox.setObjectName('BaseTextEvalCheckBox')
        self.BaseTextEvalCheckBox.setText('启用eval')

        # No Load File Support
        self.BaseDoNotLoadFileCheckBox = uni_Widget.ICTFECheckBox(self)
        self.BaseDoNotLoadFileCheckBox.setGeometry(180, 135, 120, 40)
        self.BaseDoNotLoadFileCheckBox.setObjectName('BaseDoNotLoadFileCheckBox')
        self.BaseDoNotLoadFileCheckBox.setText('大文件')

        # base table edit box and label
        self.BaseTableTips = uni_Widget.ICTFELabel(self)
        self.BaseTableTips.setObjectName('BaseTableTips')
        self.BaseTableTips.setText('编码表:')
        self.BaseTableTips.setGeometry(QtCore.QRect(50, 70, 130, 45))
        
        self.BaseTableBox = uni_Widget.ICTFELineBox(self)
        self.BaseTableBox.setObjectName('BaseTableBox')
        self.BaseTableBox.setGeometry(QtCore.QRect(150, 70, 1000, 45))
        # base enc button
        self.BaseEncButton = uni_Widget.ICTFEButton(self)
        self.BaseEncButton.setObjectName('BaseEncButton')
        self.BaseEncButton.setGeometry(QtCore.QRect(1160, 70, 120, 45))
        self.BaseEncButton.setText('编码')

        # base dec button
        self.BaseDecButton = uni_Widget.ICTFEButton(self)
        self.BaseDecButton.setObjectName('BaseDecButton')
        self.BaseDecButton.setGeometry(QtCore.QRect(1280, 70, 120, 45))
        self.BaseDecButton.setText('解码')

        # input text file button
        self.BaseTextInputPath = ''
        self.BaseTextInputButton = uni_Widget.ICTFEButton(self)
        self.BaseTextInputButton.setObjectName('BaseTextInputButton')
        self.BaseTextInputButton.setGeometry(QtCore.QRect(20, 125, 120, 45))
        self.BaseTextInputButton.setText('打开...')
        self.BaseTextInputButton.setToolTip('点击选择文件')

        # output text file button
        self.BaseTextOutputPath = ''
        self.BaseTextOutputButton = uni_Widget.ICTFEButton(self)
        self.BaseTextOutputButton.setObjectName('BaseTextOutputButton')
        self.BaseTextOutputButton.setGeometry(QtCore.QRect(320, 125, 120, 45))
        self.BaseTextOutputButton.setText('另存为...')
        self.BaseTextOutputButton.setToolTip('点击选择文件')

        # input cipher file button
        self.BaseCipherInputPath = ''
        self.BaseCipherInputButton = uni_Widget.ICTFEButton(self)
        self.BaseCipherInputButton.setObjectName('BaseCipherInputButton')
        self.BaseCipherInputButton.setGeometry(QtCore.QRect(760, 125, 120, 45))
        self.BaseCipherInputButton.setText('打开...')
        self.BaseCipherInputButton.setToolTip('点击选择文件')

        # output cipher file button
        self.BaseCipherOutputPath = ''
        self.BaseCipherOutputButton = uni_Widget.ICTFEButton(self)
        self.BaseCipherOutputButton.setObjectName('BaseCipherOutputButton')
        self.BaseCipherOutputButton.setGeometry(
            QtCore.QRect(1080, 125, 120, 45))
        self.BaseCipherOutputButton.setText('另存为...')
        self.BaseCipherOutputButton.setToolTip('点击选择文件')

        # base text box and cipher box
        self.BaseTextBox = uni_Widget.ICTFETextBox(self)
        self.BaseTextBox.setObjectName('BaseTextBox')
        self.BaseTextBox.setGeometry(QtCore.QRect(20, 180, 640, 430))
        self.BaseTextBox.setPlaceholderText('Base Encode\n这里写明文')

        self.BaseTranslateButton = uni_Widget.ICTFEButton(self)
        self.BaseTranslateButton.setObjectName('BaseTranslateButton')
        self.BaseTranslateButton.setGeometry(QtCore.QRect(665, 330, 90, 45))
        self.BaseTranslateButton.setText('交换')

        self.BaseAutoLoadCheckBox = uni_Widget.ICTFECheckBox(self)
        self.BaseAutoLoadCheckBox.setObjectName('BaseAutoLoadCheckBox')
        self.BaseAutoLoadCheckBox.setGeometry(QtCore.QRect(665, 385, 90, 45))
        self.BaseAutoLoadCheckBox.setText('Auto')

        self.BaseCipherBox = uni_Widget.ICTFETextBox(self)
        self.BaseCipherBox.setObjectName('BaseTextBox')
        self.BaseCipherBox.setGeometry(QtCore.QRect(760, 180, 640, 430))
        self.BaseCipherBox.setPlaceholderText('Base Decode\n这里写编码')

        # end base panel
