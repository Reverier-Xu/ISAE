from PyQt5 import QtWidgets, QtGui, QtCore


class ICTFEButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(ICTFEButton, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            "QPushButton{"
            "background-color:rgb(40, 40, 40);"
            "color:rgb(200,200,200);"
            "border-width:1px;"
            "border-color:rgb(50,50,50);"
            "}")
        self.setFlat(True)


class ICTFETextBox(QtWidgets.QTextEdit):
    def __init__(self,parent=None):
        super(ICTFETextBox, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("consolas")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.setTextColor(QtGui.QColor(200, 200, 200))
        self.setAcceptDrops(True)
        self.setAcceptRichText(False)


class ICTFELineBox(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(ICTFELineBox, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("consolas")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            'color: white;'
            'border: 2px solid gray;'
            'border-radius: 10px;'
            'padding: 0 8px;'
            'background: rgb(20, 20, 20);'
            'selection-background-color: blue;')


class ICTFECheckBox(QtWidgets.QCheckBox):
    def __init__(self, parent=None):
        super(ICTFECheckBox, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            'QCheckBox:unchecked{ border:none; color: white; }'
            'QCheckBox:checked{ border:none; color: cyan; }')


class ICTFELabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(ICTFELabel, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet('color: white;')


class ICTFEList(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(ICTFEList, self).__init__(parent)
        self.setStyleSheet(
            '#FileTempStack{'
            'background-color: rgb(20,20,20);'
            'color: white'
            '}')
        font = QtGui.QFont()
        font.setFamily("consolas")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
