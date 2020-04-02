from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Widgets import uni_Widget


class ui_RSAPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_RSAPanel, self).__init__()

        # Crypto Buttons area

        self.RSAMode = 0
        self.rsaChoosePanel = QtWidgets.QWidget()
        self.rsaChoosePanel.setObjectName('rsaChoosePanel')
        self.rsaChoosePanel.setStyleSheet('#rsaChoosePanel{background-color: transparent}')
        self.rsaChoosePanel.setGeometry(0, 0, 1199, 300)

        self.rsaChoosePanelScroll = uni_Widget.ICTFEScrollArea(self)
        self.rsaChoosePanelScroll.setGeometry(QtCore.QRect(0, 0, 1100, 65))
        self.rsaChoosePanelScroll.setWidget(self.rsaChoosePanel)

        # blue tiaotiao
        self.RSAMode = 1
        self.RSAChooserBox = [0, 50, 240, 480, 710, 910]
        self.RSAChooser = QtWidgets.QLabel(self.rsaChoosePanel)
        self.RSAChooser.setPixmap(
            QtGui.QPixmap('./Resources/chooser.png'))
        self.RSAChooser.setGeometry(QtCore.QRect(
            self.RSAChooserBox[self.RSAMode], 55, 140, 8))

        # rsa change Buttons
        self.epqButton = uni_Widget.ICTFEButton(self.rsaChoosePanel)
        self.epqButton.setObjectName('epqButton')
        self.epqButton.setGeometry(QtCore.QRect(10, 10, 190, 45))
        self.epqButton.setText('已知e、p、q')

        self.dnButton = uni_Widget.ICTFEButton(self.rsaChoosePanel)
        self.dnButton.setObjectName('ednButton')
        self.dnButton.setGeometry(QtCore.QRect(210, 10, 190, 45))
        self.dnButton.setText('已知d、n')

        self.dpdqpqButton = uni_Widget.ICTFEButton(self.rsaChoosePanel)
        self.dpdqpqButton.setObjectName('edpdqpqButton')
        self.dpdqpqButton.setGeometry(QtCore.QRect(410, 10, 250, 45))
        self.dpdqpqButton.setText('已知dp、dq、p、q')

        self.edpnButton = uni_Widget.ICTFEButton(self.rsaChoosePanel)
        self.edpnButton.setObjectName('edpnButton')
        self.edpnButton.setGeometry(QtCore.QRect(670, 10, 190, 45))
        self.edpnButton.setText('已知e、dp、n')

        self.rabinButton = uni_Widget.ICTFEButton(self.rsaChoosePanel)
        self.rabinButton.setObjectName('rabinButton')
        self.rabinButton.setGeometry(QtCore.QRect(870, 10, 190, 45))
        self.rabinButton.setText('rabin attack')

        # end rsa change buttons

        # 校验器
        reg = QtCore.QRegExp('[0-9a-fA-F]*')
        validator = QtGui.QRegExpValidator(self)
        validator.setRegExp(reg)

        # RSA Decrypt button
        self.RSAattackButton = uni_Widget.ICTFEButton(self)
        self.RSAattackButton.setObjectName('RSAattacktButton')
        self.RSAattackButton.setGeometry(
            QtCore.QRect(1180, 10, 220, 45))
        self.RSAattackButton.setText('attack!')



        # RSA Encode button

        self.RSAcBox = uni_Widget.ICTFELineBox(self)
        self.RSAcBox.setObjectName('RSAcBox')
        self.RSAcBox.setGeometry(QtCore.QRect(20, 80, 1380, 50))
        self.RSAcBox.setPlaceholderText('RSA C:')
        self.RSAcBox.setValidator(validator)
        self.RSAcBox.setEnabled(False)

        self.RSApBox = uni_Widget.ICTFELineBox(self)
        self.RSApBox.setObjectName('RSApBox')
        self.RSApBox.setGeometry(QtCore.QRect(20, 140, 1380, 50))
        self.RSApBox.setPlaceholderText('RSA p:')
        self.RSApBox.setValidator(validator)
        self.RSApBox.setEnabled(False)

        self.RSAqBox = uni_Widget.ICTFELineBox(self)
        self.RSAqBox.setObjectName('RSAqBox')
        self.RSAqBox.setGeometry(QtCore.QRect(20, 200, 1380, 50))
        self.RSAqBox.setPlaceholderText('RSA q:')
        self.RSAqBox.setValidator(validator)
        self.RSAqBox.setEnabled(False)

        self.RSAnBox = uni_Widget.ICTFELineBox(self)
        self.RSAnBox.setObjectName('RSAnBox')
        self.RSAnBox.setGeometry(QtCore.QRect(20, 260, 1380, 50))
        self.RSAnBox.setPlaceholderText('RSA n:')
        self.RSAnBox.setValidator(validator)
        self.RSAnBox.setEnabled(False)

        self.RSAeBox = uni_Widget.ICTFELineBox(self)
        self.RSAeBox.setObjectName('RSAeBox')
        self.RSAeBox.setGeometry(QtCore.QRect(20, 320, 1380, 50))
        self.RSAeBox.setPlaceholderText('RSA e:')
        self.RSAeBox.setValidator(validator)
        self.RSAeBox.setEnabled(False)

        self.RSAdBox = uni_Widget.ICTFELineBox(self)
        self.RSAdBox.setObjectName('RSAdBox')
        self.RSAdBox.setGeometry(QtCore.QRect(20, 380, 1380, 50))
        self.RSAdBox.setPlaceholderText('RSA d:')
        self.RSAdBox.setValidator(validator)
        self.RSAdBox.setEnabled(False)


        self.RSAdpBox = uni_Widget.ICTFELineBox(self)
        self.RSAdpBox.setObjectName('RSAdpBox')
        self.RSAdpBox.setGeometry(QtCore.QRect(20, 440, 1380, 50))
        self.RSAdpBox.setPlaceholderText('RSA dp:')
        self.RSAdpBox.setValidator(validator)
        self.RSAdBox.setEnabled(False)

        self.RSAdqBox = uni_Widget.ICTFELineBox(self)
        self.RSAdqBox.setObjectName('RSAdqBox')
        self.RSAdqBox.setGeometry(QtCore.QRect(20, 500, 1380, 50))
        self.RSAdqBox.setPlaceholderText('RSA dq:')
        self.RSAdqBox.setValidator(validator)
        self.RSAdqBox.setEnabled(False)

        self.RSAmBox = uni_Widget.ICTFELineBox(self)
        self.RSAmBox.setObjectName('RSAmBox')
        self.RSAmBox.setGeometry(QtCore.QRect(20, 560, 1380, 50))
        self.RSAmBox.setPlaceholderText('RSA m:')
        self.RSAmBox.setValidator(validator)
        self.RSAmBox.setEnabled(False)

        # end RSA panel
