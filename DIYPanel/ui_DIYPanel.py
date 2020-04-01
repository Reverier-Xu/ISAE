from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenu

from ui_Widgets import ErrorWin, uni_Widget


class ui_DIYPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_DIYPanel, self).__init__()
        self.ButtonArea = DIYedPanel(self)
        self.ButtonArea.setGeometry(QtCore.QRect(0, 0, 1426, 128))
        self.ButtonArea.ButtonScroll.setGeometry(QtCore.QRect(0, 0, 1426, 128))

        self.Panels = []


class DIYedPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DIYedPanel, self).__init__(parent)
        self.ButtonScroll = uni_Widget.ICTFEScrollArea(self)
        self.ButtonScroll.setObjectName('ButtonScroll')
        self.ButtonPanel = CostumedPanel()
        self.ButtonPanel.setGeometry(QtCore.QRect(0, 0, 1426, 128))
        self.ButtonPanel.setObjectName('ButtonPanel')
        self.ButtonScroll.setWidget(self.ButtonPanel)

        self.TheAddButton = uni_Widget.ICTFEButton(self.ButtonPanel)
        self.TheAddButton.setObjectName('addButton')
        self.TheAddButton.setGeometry(QtCore.QRect(0, 0, 128, 128))
        font = QtGui.QFont()
        font.setFamily('consolas')
        font.setPixelSize(50)
        self.TheAddButton.setFont(font)
        self.TheAddButton.setText('+')

        self.DIYPanelStacks = QtWidgets.QStackedWidget(self)
        self.DIYPanelStacks.setObjectName('DIYPanelStacks')
        self.DIYPanelStacks.setGeometry(QtCore.QRect(1, 135, 1423, 613))

        self.TheAddButton.clicked.connect(self.addOne)
        self.ButtonPanel.reArrangeButtonSig.connect(self.reArrangeAddButton)

    def addOne(self):
        text, ok = QtWidgets.QInputDialog.getText(self, '创建分区', '名称')
        if ok:
            self.ButtonPanel.addButton(str(text))
            animation = QtCore.QPropertyAnimation(self)
            animation.setTargetObject(self.TheAddButton)
            animation.setPropertyName(b'pos')
            animation.setDuration(150)
            animation.setStartValue(self.TheAddButton.pos())
            animation.setEndValue(QtCore.QPoint(self.ButtonPanel.VBox[len(self.ButtonPanel.Buttons) % 11],
                                                self.ButtonPanel.HBox[len(self.ButtonPanel.Buttons) // 11]))
            animation.start()

    def reArrangeAddButton(self):
        animation = QtCore.QPropertyAnimation(self)
        animation.setTargetObject(self.TheAddButton)
        animation.setPropertyName(b'pos')
        animation.setDuration(150)
        animation.setStartValue(self.TheAddButton.pos())
        animation.setEndValue(QtCore.QPoint(self.ButtonPanel.VBox[len(self.ButtonPanel.Buttons) % 11],
                                            self.ButtonPanel.HBox[len(self.ButtonPanel.Buttons) // 11]))
        animation.start()


class CostumedPanel(QtWidgets.QWidget):
    reArrangeButtonSig = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(CostumedPanel, self).__init__(parent)
        self.row = 1
        self.VBox = [0, 128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280]
        self.HBox = [0, 128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280]
        self.setStyleSheet('background-color: transparent;')
        self.Buttons = []

    def addButton(self, text):
        self.Buttons.append(DIYedButton(self))
        id = len(self.Buttons) - 1
        r = id // 11
        w = id % 11
        self.Buttons[id].setGeometry(QtCore.QRect(self.VBox[w], self.HBox[r], 128, 128))
        self.Buttons[id].setObjectName(text)
        self.Buttons[id].setText(text)
        if len(self.Buttons) // 11 + 1 != self.row:
            self.row = len(self.Buttons) // 11 + 1
            self.setGeometry(QtCore.QRect(0, 0, 1426, self.VBox[self.row]))
        self.Buttons[id].show()
        self.Buttons[id].Deleted.connect(self.reArrangeButtons)

    def reArrangeButtons(self):
        endOne = len(self.Buttons) - 1
        for i in range(0, len(self.Buttons) - 1, 1):
            if self.Buttons[i].isEnabled() is False:
                self.Buttons[i].deleteLater()
                self.Buttons.remove(self.Buttons[i])
            animation = QtCore.QPropertyAnimation(self)
            animation.setDuration(150)
            animation.setPropertyName(b'pos')
            animation.setTargetObject(self.Buttons[i])
            animation.setStartValue(self.Buttons[i].pos())
            r = i // 11
            w = i % 11
            animation.setEndValue(QtCore.QPoint(self.VBox[w], self.HBox[r]))
            animation.start()
        try:
            if self.Buttons[endOne].isEnabled() is False:
                self.Buttons[endOne].deleteLater()
                self.Buttons.remove(self.Buttons[endOne])
        except:
            pass
        self.reArrangeButtonSig.emit()


class DIYedButton(uni_Widget.ICTFEButton):
    Deleted = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(DIYedButton, self).__init__(parent)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        quitAction = menu.addAction("Delete")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAction:
            self.setEnabled(False)
            self.Deleted.emit()
