from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Widgets import uni_Widget


class ui_QuotePanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_QuotePanel, self).__init__()
        # begin quote panel
        # input text file button
        self.QuoteTextInputPath = ''
        self.QuoteTextInputButton = uni_Widget.ICTFEButton(self)
        self.QuoteTextInputButton.setObjectName('QuoteTextInputButton')
        self.QuoteTextInputButton.setGeometry(QtCore.QRect(20, 20, 120, 45))
        self.QuoteTextInputButton.setText('打开...')
        self.QuoteTextInputButton.setToolTip('点击选择文件')

        # output text file button
        self.QuoteTextOutputPath = ''
        self.QuoteTextOutputButton = uni_Widget.ICTFEButton(self)
        self.QuoteTextOutputButton.setObjectName('QuoteTextOutputButton')
        self.QuoteTextOutputButton.setGeometry(QtCore.QRect(260, 20, 120, 45))
        self.QuoteTextOutputButton.setText('另存为...')
        self.QuoteTextOutputButton.setToolTip('点击选择文件')

        # eval support
        self.QuoteTextEvalCheckBox = uni_Widget.ICTFECheckBox(self)
        self.QuoteTextEvalCheckBox.setGeometry(QtCore.QRect(450, 35, 120, 40))
        self.QuoteTextEvalCheckBox.setObjectName('QuoteTextEvalCheckBox')
        self.QuoteTextEvalCheckBox.setText('启用eval')

        # Quote Encode button
        self.QuoteEncodeButton = uni_Widget.ICTFEButton(self)
        self.QuoteEncodeButton.setObjectName('QuoteEncodeButton')
        self.QuoteEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.QuoteEncodeButton.setText('编码')

        # input cipher file button
        self.QuoteCipherInputPath = ''
        self.QuoteCipherInputButton = uni_Widget.ICTFEButton(self)
        self.QuoteCipherInputButton.setObjectName('QuoteCipherInputButton')
        self.QuoteCipherInputButton.setGeometry(
            QtCore.QRect(720, 20, 120, 45))
        self.QuoteCipherInputButton.setText('打开...')
        self.QuoteCipherInputButton.setToolTip('点击选择文件')

        # output cipher file button
        self.QuoteCipherOutputPath = ''
        self.QuoteCipherOutputButton = uni_Widget.ICTFEButton(self)
        self.QuoteCipherOutputButton.setObjectName('QuoteCipherOutputButton')
        self.QuoteCipherOutputButton.setGeometry(
            QtCore.QRect(960, 20, 120, 45))
        self.QuoteCipherOutputButton.setText('另存为...')
        self.QuoteCipherOutputButton.setToolTip('点击选择文件')

        # Quote Decode button
        self.QuoteDecodeButton = uni_Widget.ICTFEButton(self)
        self.QuoteDecodeButton.setObjectName('QuoteDecodeButton')
        self.QuoteDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.QuoteDecodeButton.setText('解码')

        self.QuoteTextBox = uni_Widget.ICTFETextBox(self)
        self.QuoteTextBox.setObjectName('QuoteTextBox')
        self.QuoteTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.QuoteTextBox.setPlaceholderText('Quote - Printable\n这里写明文')

        self.QuoteCipherBox = uni_Widget.ICTFETextBox(self)
        self.QuoteCipherBox.setObjectName('QuoteCipherBox')
        self.QuoteCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.QuoteCipherBox.setPlaceholderText('Quote - Printable\n这里写编码')
        # end quote panel
