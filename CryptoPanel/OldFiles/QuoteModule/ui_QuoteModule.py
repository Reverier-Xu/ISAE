from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Widgets import uni_Widget


class ui_QuotePanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_QuotePanel, self).__init__()
        # begin quote panel
        # input text file button
        self.QuoteTextInputPath = ''

        # output text file button
        self.QuoteTextOutputPath = ''

        # input cipher file button
        self.QuoteCipherInputPath = ''

        # output cipher file button
        self.QuoteCipherOutputPath = ''

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.QuoteTextInputButton = uni_Widget.ICTFEButton(self)
        self.QuoteTextInputButton.setMinimumSize(QtCore.QSize(120, 45))
        self.QuoteTextInputButton.setMaximumSize(QtCore.QSize(120, 45))
        self.QuoteTextInputButton.setObjectName("QuoteTextInputButton")
        self.horizontalLayout.addWidget(self.QuoteTextInputButton)
        self.QuoteTextOutputButton = uni_Widget.ICTFEButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.QuoteTextOutputButton.sizePolicy().hasHeightForWidth())
        self.QuoteTextOutputButton.setSizePolicy(sizePolicy)
        self.QuoteTextOutputButton.setMinimumSize(QtCore.QSize(120, 45))
        self.QuoteTextOutputButton.setMaximumSize(QtCore.QSize(120, 45))
        self.QuoteTextOutputButton.setObjectName("QuoteTextOutputButton")
        self.horizontalLayout.addWidget(self.QuoteTextOutputButton)
        self.QuoteEvalCheckBox = uni_Widget.ICTFECheckBox(self)
        self.QuoteEvalCheckBox.setMinimumSize(QtCore.QSize(120, 45))
        self.QuoteEvalCheckBox.setMaximumSize(QtCore.QSize(120, 45))
        self.QuoteEvalCheckBox.setObjectName("QuoteEvalCheckBox")
        self.horizontalLayout.addWidget(self.QuoteEvalCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.QuoteEncodeButton = uni_Widget.ICTFEButton(self)
        self.QuoteEncodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.QuoteEncodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.QuoteEncodeButton.setObjectName("QuoteEncodeButton")
        self.horizontalLayout.addWidget(self.QuoteEncodeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.QuoteTextBox = uni_Widget.ICTFETextBox(self)
        self.QuoteTextBox.setObjectName("QuoteTextBox")
        self.verticalLayout.addWidget(self.QuoteTextBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.QuoteCipherInputButton = uni_Widget.ICTFEButton(self)
        self.QuoteCipherInputButton.setMinimumSize(QtCore.QSize(120, 45))
        self.QuoteCipherInputButton.setMaximumSize(QtCore.QSize(120, 45))
        self.QuoteCipherInputButton.setObjectName("QuoteCipherInputButton")
        self.horizontalLayout_2.addWidget(self.QuoteCipherInputButton)
        self.QuoteCipherOutputButton = uni_Widget.ICTFEButton(self)
        self.QuoteCipherOutputButton.setMinimumSize(QtCore.QSize(120, 45))
        self.QuoteCipherOutputButton.setMaximumSize(QtCore.QSize(120, 45))
        self.QuoteCipherOutputButton.setObjectName("QuoteCipherOutputButton")
        self.horizontalLayout_2.addWidget(self.QuoteCipherOutputButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.QuoteDecodeButton = uni_Widget.ICTFEButton(self)
        self.QuoteDecodeButton.setMinimumSize(QtCore.QSize(120, 45))
        self.QuoteDecodeButton.setMaximumSize(QtCore.QSize(120, 45))
        self.QuoteDecodeButton.setObjectName("QuoteDecodeButton")
        self.horizontalLayout_2.addWidget(self.QuoteDecodeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.QuoteCipherBox = uni_Widget.ICTFETextBox(self)
        self.QuoteCipherBox.setObjectName("QuoteCipherBox")
        self.verticalLayout_2.addWidget(self.QuoteCipherBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.QuoteTextInputButton.setText(_translate("self", "打开"))
        self.QuoteTextOutputButton.setText(_translate("self", "另存为"))
        self.QuoteEvalCheckBox.setText(_translate("self", "启用eval"))
        self.QuoteEncodeButton.setText(_translate("self", "编码"))
        self.QuoteCipherInputButton.setText(_translate("self", "打开"))
        self.QuoteCipherOutputButton.setText(_translate("self", "另存为"))
        self.QuoteDecodeButton.setText(_translate("self", "解码"))

        # end quote panel
