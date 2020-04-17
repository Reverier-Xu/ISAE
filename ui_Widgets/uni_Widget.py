from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

ButtonStyleNormal = "QPushButton{" \
                    "background-color:rgba(30, 30, 30, 100%);" \
                    "color: white;" \
                    "border-radius: 0px;" \
                    "border: 0px groove gray;" \
                    "border-style: outset;" \
                    "}" \
                    "QPushButton:hover{" \
                    "background-color: rgba(50, 50, 50, 100%);" \
                    "color: white;" \
                    "}" \
                    "QPushButton:pressed{" \
                    "background-color: rgb(80, 80, 80);" \
                    "border-style: inset; " \
                    "}"

ButtonStyleSelected = "QPushButton{" \
                      "background-color:rgba(40, 140, 255, 100%);" \
                      "color: white;" \
                      "border-radius: 0px;" \
                      "border: 0px groove gray;" \
                      "border-style: outset;" \
                      "}" \
                      "QPushButton:hover{" \
                      "background-color: rgba(60, 60, 255, 100%);" \
                      "color: white;" \
                      "}" \
                      "QPushButton:pressed{" \
                      "background-color: rgb(100, 100, 255);" \
                      "border-style: inset; " \
                      "}"
ButtonStyleBlue = "QPushButton{" \
                  "background-color:rgba(40, 140, 255, 100%);" \
                  "color: white;" \
                  "border-radius: 0px;" \
                  "border: 0px groove gray;" \
                  "border-style: outset;" \
                  "}" \
                  "QPushButton:hover{" \
                  "background-color: rgba(60, 60, 255, 100%);" \
                  "color: white;" \
                  "}" \
                  "QPushButton:pressed{" \
                  "background-color: rgb(100, 100, 255);" \
                  "border-style: inset; " \
                  "}"
ButtonStyleYellow = "QPushButton{" \
                    "background-color:rgba(240, 145, 40, 100%);" \
                    "color: white;" \
                    "border-radius: 0px;" \
                    "border: 0px groove gray;" \
                    "border-style: outset;" \
                    "}" \
                    "QPushButton:hover{" \
                    "background-color: rgba(160, 145, 60, 100%);" \
                    "color: white;" \
                    "}" \
                    "QPushButton:pressed{" \
                    "background-color: rgb(160, 115, 60);" \
                    "border-style: inset; " \
                    "}"
ButtonStyleRed = "QPushButton{" \
    "background-color:rgba(250, 40, 155, 100%);" \
    "color: white;" \
    "border-radius: 0px;" \
    "border: 0px groove gray;" \
    "border-style: outset;" \
    "}" \
    "QPushButton:hover{" \
    "background-color: rgba(255, 60, 60, 100%);" \
    "color: white;" \
    "}" \
    "QPushButton:pressed{" \
    "background-color: rgb(100, 100, 255);" \
    "border-style: inset; " \
    "}"
ButtonStyleGreen = "QPushButton{" \
    "background-color:rgba(60, 180, 75, 100%);" \
    "color: white;" \
    "border-radius: 0px;" \
    "border: 0px groove gray;" \
    "border-style: outset;" \
    "}" \
    "QPushButton:hover{" \
    "background-color: rgba(60, 165, 60, 100%);" \
    "color: white;" \
    "}" \
    "QPushButton:pressed{" \
    "background-color: rgb(30, 225, 30);" \
    "border-style: inset; " \
    "}"
SplitterBlue = "QWidget{\n"\
    "background-color: rgba(40, 140, 255, 100%);\n"\
    "border: 1px rgba(40, 140, 255, 100%);\n"\
    "border-style: solid;\n"\
    "}"
SplitterRed = "QWidget{\n"\
    "background-color: rgba(250, 40, 155, 100%);\n"\
    "border: 1px rgba(250, 40, 155, 100%);\n"\
    "border-style: solid;\n"\
    "}"
SplitterYellow = "QWidget{\n"\
    "background-color: rgba(240, 145, 40, 100%);\n"\
    "border: 1px rgba(240, 145, 40, 100%);\n"\
    "border-style: solid;\n"\
    "}"
SplitterGreen = "QWidget{\n"\
    "background-color: rgba(60, 180, 75, 100%);\n"\
    "border: 1px rgba(60, 180, 75, 100%);\n"\
    "border-style: solid;\n"\
    "}"
ButtonStyles = [ButtonStyleBlue, ButtonStyleGreen,
                ButtonStyleRed, ButtonStyleYellow]
SplitterStyles = [SplitterBlue, SplitterGreen, SplitterRed, SplitterYellow]


class ICTFESplitter(QtWidgets.QSplitter):
    def __init__(self, parent=None):
        super(ICTFESplitter, self).__init__(parent)
        self.setStyleSheet("QSplitter::handle {"
                           "background-color: rgb(50, 50, 50);"
                           "}"
                           "QSplitter::handle:horizontal {"
                           "width: 3px;"
                           "}"
                           "QSplitter::handle:vertical {"
                           "height: 3px;"
                           "}"
                           "QSplitter::handle:pressed {"
                           "background-color: rgb(50, 250, 150);"
                           "}"
                           "QSplitter::handle:hover {"
                           "background-color: rgb(50, 150, 250);"
                           "}")


class ICTFEButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(ICTFEButton, self).__init__(parent)
        self.setMinimumSize(120, 32)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPixelSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            "QPushButton{"
            "background-color:rgba(30, 30, 30, 100%);"
            "color: white;"
            "border-radius: 0px;"
            "border: 0px groove gray;"
            "border-style: outset;"
            "}"
            "QPushButton:hover{"
            "background-color: rgba(50, 50, 50, 100%);"
            "color: white;"
            "}"
            "QPushButton:pressed{"
            "background-color: rgb(80, 80, 80);"
            "border-style: inset; "
            "}")


class ICTFETextBox(QtWidgets.QTextEdit):
    def __init__(self, parent=None):
        super(ICTFETextBox, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("consolas")
        font.setPixelSize(24)
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
        font.setPixelSize(24)
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
        self.setDragEnabled(True)


class ICTFECheckBox(QtWidgets.QCheckBox):
    def __init__(self, parent=None):
        super(ICTFECheckBox, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPixelSize(22)
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
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet('color: white;')


class ICTFEList(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(ICTFEList, self).__init__(parent)
        self.setStyleSheet(
            'QListWidget{'
            'background-color: rgb(30, 30, 30);'
            'border: 1px solid grey;'
            'color: white;'
            '}')
        font = QtGui.QFont()
        font.setFamily("consolas")
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setDragEnabled(True)
        self.setDefaultDropAction(Qt.TargetMoveAction)

    def dragEnterEvent(self, e):
        e.accept()


class ICTFEScrollArea(QtWidgets.QScrollArea):
    def __init__(self, parent=None):
        super(ICTFEScrollArea, self).__init__(parent)
        self.setStyleSheet(
            'QScrollArea{'
            'border: none;'
            'background-color:rgb(30, 30, 30);'
            '}')
        self.viewport().setStyleSheet(
            'QScrollArea{'
            'border: none;'
            'background-color:rgb(30, 30, 30);'
            '}')
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
