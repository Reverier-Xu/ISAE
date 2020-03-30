from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_HashPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_HashPanel, self).__init__()

        # input text file button
        self.HashTextInputPath = ''
        self.HashTextInputButton = uni_Widget.ICTFEButton(self)
        self.HashTextInputButton.setObjectName('HashTextInputButton')
        self.HashTextInputButton.setGeometry(QtCore.QRect(20, 20, 120, 45))
        self.HashTextInputButton.setText('打开...')
        self.HashTextInputButton.setToolTip('点击选择文件')

        # Hash Encode button
        self.HashEncodeButton = uni_Widget.ICTFEButton(self)
        self.HashEncodeButton.setObjectName('HashEncodeButton')
        self.HashEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.HashEncodeButton.setText('计算')

        self.HashTextBox = uni_Widget.ICTFETextBox(self)
        self.HashTextBox.setObjectName('HashTextBox')
        self.HashTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.HashTextBox.setPlaceholderText('Hash Calculate\n这里写明文')

        self.HashEvalCheckBox = uni_Widget.ICTFECheckBox(self)
        self.HashEvalCheckBox.setObjectName('HashEvalCheckBox')
        self.HashEvalCheckBox.setGeometry(QtCore.QRect(150, 25, 120, 45))
        self.HashEvalCheckBox.setText('eval')

        self.ResultArea = QtWidgets.QWidget()
        self.ResultArea.setObjectName('ResultArea')
        self.ResultArea.setGeometry(QtCore.QRect(700, 80, 720, 1000))
        self.ResultArea.setStyleSheet('#ResultArea{background-color: transparent}')

        self.ResultAreaScroll = uni_Widget.ICTFEScrollArea(self)
        self.ResultAreaScroll.setObjectName('ResultAreaScroll')
        self.ResultAreaScroll.setGeometry(QtCore.QRect(700, 80, 720, 530))
        self.ResultAreaScroll.setWidget(self.ResultArea)

        self.HashTips = uni_Widget.ICTFELabel(self.ResultArea)
        self.HashTips.setObjectName('HashTips')
        self.HashTips.setGeometry(QtCore.QRect(15, 5, 80, 45))
        self.HashTips.setText('Hash:')
        self.HashValueBox = uni_Widget.ICTFELineBox(self.ResultArea)
        self.HashValueBox.setObjectName('HashValueBox')
        self.HashValueBox.setGeometry(QtCore.QRect(15, 50, 680, 45))

        self.MD5Tips = uni_Widget.ICTFELabel(self.ResultArea)
        self.MD5Tips.setObjectName('MD5Tips')
        self.MD5Tips.setGeometry(QtCore.QRect(15, 95, 80, 45))
        self.MD5Tips.setText('MD5:')
        self.MD5ValueBox = uni_Widget.ICTFELineBox(self.ResultArea)
        self.MD5ValueBox.setObjectName('MD5ValueBox')
        self.MD5ValueBox.setGeometry(QtCore.QRect(15, 140, 680, 45))

        self.SHA1Tips = uni_Widget.ICTFELabel(self.ResultArea)
        self.SHA1Tips.setObjectName('SHA1Tips')
        self.SHA1Tips.setGeometry(QtCore.QRect(15, 185, 80, 45))
        self.SHA1Tips.setText('SHA1:')
        self.SHA1ValueBox = uni_Widget.ICTFELineBox(self.ResultArea)
        self.SHA1ValueBox.setObjectName('SHA1ValueBox')
        self.SHA1ValueBox.setGeometry(QtCore.QRect(15, 230, 680, 45))

        self.SHA224Tips = uni_Widget.ICTFELabel(self.ResultArea)
        self.SHA224Tips.setObjectName('SHA224Tips')
        self.SHA224Tips.setGeometry(QtCore.QRect(15, 275, 95, 45))
        self.SHA224Tips.setText('SHA224:')
        self.SHA224ValueBox = uni_Widget.ICTFELineBox(self.ResultArea)
        self.SHA224ValueBox.setObjectName('SHA224ValueBox')
        self.SHA224ValueBox.setGeometry(QtCore.QRect(15, 320, 680, 45))

        self.SHA256Tips = uni_Widget.ICTFELabel(self.ResultArea)
        self.SHA256Tips.setObjectName('SHA256Tips')
        self.SHA256Tips.setGeometry(QtCore.QRect(15, 365, 95, 45))
        self.SHA256Tips.setText('SHA256:')
        self.SHA256ValueBox = uni_Widget.ICTFELineBox(self.ResultArea)
        self.SHA256ValueBox.setObjectName('SHA256ValueBox')
        self.SHA256ValueBox.setGeometry(QtCore.QRect(15, 410, 680, 45))

        self.SHA384Tips = uni_Widget.ICTFELabel(self.ResultArea)
        self.SHA384Tips.setObjectName('SHA384Tips')
        self.SHA384Tips.setGeometry(QtCore.QRect(15, 455, 95, 45))
        self.SHA384Tips.setText('SHA384:')
        self.SHA384ValueBox = uni_Widget.ICTFELineBox(self.ResultArea)
        self.SHA384ValueBox.setObjectName('SHA384ValueBox')
        self.SHA384ValueBox.setGeometry(QtCore.QRect(15, 500, 680, 45))

        self.SHA512Tips = uni_Widget.ICTFELabel(self.ResultArea)
        self.SHA512Tips.setObjectName('SHA512Tips')
        self.SHA512Tips.setGeometry(QtCore.QRect(15, 545, 95, 45))
        self.SHA512Tips.setText('SHA512:')
        self.SHA512ValueBox = uni_Widget.ICTFELineBox(self.ResultArea)
        self.SHA512ValueBox.setObjectName('SHA512ValueBox')
        self.SHA512ValueBox.setGeometry(QtCore.QRect(15, 590, 680, 45))

        self.SHA3224Tips = uni_Widget.ICTFELabel(self.ResultArea)
        self.SHA3224Tips.setObjectName('SHA3224Tips')
        self.SHA3224Tips.setGeometry(QtCore.QRect(15, 635, 180, 45))
        self.SHA3224Tips.setText('SHA3_224:')
        self.SHA3224ValueBox = uni_Widget.ICTFELineBox(self.ResultArea)
        self.SHA3224ValueBox.setObjectName('SHA3224ValueBox')
        self.SHA3224ValueBox.setGeometry(QtCore.QRect(15, 680, 680, 45))

        self.SHA3256Tips = uni_Widget.ICTFELabel(self.ResultArea)
        self.SHA3256Tips.setObjectName('SHA3256Tips')
        self.SHA3256Tips.setGeometry(QtCore.QRect(15, 725, 180, 45))
        self.SHA3256Tips.setText('SHA3_256:')
        self.SHA3256ValueBox = uni_Widget.ICTFELineBox(self.ResultArea)
        self.SHA3256ValueBox.setObjectName('SHA3256ValueBox')
        self.SHA3256ValueBox.setGeometry(QtCore.QRect(15, 770, 680, 45))

        self.SHA3384Tips = uni_Widget.ICTFELabel(self.ResultArea)
        self.SHA3384Tips.setObjectName('SHA3384Tips')
        self.SHA3384Tips.setGeometry(QtCore.QRect(15, 815, 180, 45))
        self.SHA3384Tips.setText('SHA3_384:')
        self.SHA3384ValueBox = uni_Widget.ICTFELineBox(self.ResultArea)
        self.SHA3384ValueBox.setObjectName('SHA3384ValueBox')
        self.SHA3384ValueBox.setGeometry(QtCore.QRect(15, 860, 680, 45))

        self.SHA3512Tips = uni_Widget.ICTFELabel(self.ResultArea)
        self.SHA3512Tips.setObjectName('SHA3512Tips')
        self.SHA3512Tips.setGeometry(QtCore.QRect(15, 905, 180, 45))
        self.SHA3512Tips.setText('SHA3_512:')
        self.SHA3512ValueBox = uni_Widget.ICTFELineBox(self.ResultArea)
        self.SHA3512ValueBox.setObjectName('SHA3512ValueBox')
        self.SHA3512ValueBox.setGeometry(QtCore.QRect(15, 950, 680, 45))
        # end Hash panel
