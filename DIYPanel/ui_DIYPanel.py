from PyQt5 import QtWidgets, QtCore, QtGui
from ui_Widgets import uni_Widget
import os
import platform


class ui_DIYPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ui_DIYPanel, self).__init__(parent)

        # 上层
        self.TabAreaScroll = uni_Widget.ICTFEScrollArea(self)
        self.TabAreaScroll.setObjectName('TabAreaScroll')
        self.TabAreaScroll.setGeometry(QtCore.QRect(0, 0, 1426, 128))
        self.TabAreaPanel = ResizablePanel(self)
        self.TabAreaPanel.setGeometry(QtCore.QRect(0, 0, 1426, 128))
        self.TabAreaPanel.setObjectName('TabAreaPanel')
        self.TabAreaScroll.setWidget(self.TabAreaPanel)
        self.TabAreaPanel.TheAddButton.clicked.connect(self.AddTabPanel)

        # 下层
        self.TabStack = QtWidgets.QStackedWidget(self)
        self.TabStack.setObjectName('TabStack')
        self.TabStack.setGeometry(QtCore.QRect(0, 132, 1425, 613))

        # 统一管理
        self.TabButtons = self.TabAreaPanel.Buttons  # 通过List进行有序化管理
        self.TabPanels = []
        self.FileButtons = []

    def AddTabPanel(self):
        text, ok = QtWidgets.QInputDialog.getText(self, '创建分区', '名称')
        if ok:
            button = self.TabAreaPanel.addButton(text)
            panel = ResizablePanel()
            panel.setObjectName(text)
            self.TabStack.addWidget(panel)
            self.TabPanels.append(panel)
            button.clicked.connect(lambda: self.TabStack.setCurrentWidget(panel))
            button.Deleted.connect(lambda: self.DeletePanel(panel))
            panel.TheAddButton.clicked.connect(lambda: self.AddTabPanelButton(panel))
            self.FileButtons.append(panel.Buttons)

    def AddTabPanelFile(self, text):
        button = self.TabAreaPanel.addButton(text)
        panel = ResizablePanel()
        panel.setObjectName(text)
        self.TabStack.addWidget(panel)
        self.TabPanels.append(panel)
        button.clicked.connect(lambda: self.TabStack.setCurrentWidget(panel))
        button.Deleted.connect(lambda: self.DeletePanel(panel))
        panel.TheAddButton.clicked.connect(lambda: self.AddTabPanelButton(panel))
        self.FileButtons.append(panel.Buttons)

    def AddTabPanelButton(self, panel):
        file, ok = QtWidgets.QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         '',
                                                         "All Files (*)")
        if ok:
            name, ok = QtWidgets.QInputDialog.getText(self, '创建启动按钮', '名称')
            button = panel.addButton(name)
            button.clicked.connect(lambda: self.OpenFile(file))
            button.Deleted.connect(lambda: self.DeleteTabPanelButton(panel))

    def AddTabPanelButtonFile(self, panel, file, name):
        button = panel.addButton(name)
        button.clicked.connect(lambda: self.OpenFile(file))
        button.Deleted.connect(lambda: self.DeleteTabPanelButton(panel))

    def OpenFile(self, file):
        ok = os.system(file)
        if ok != 0:
            sysstr = platform.system()
            if sysstr == 'Windows':
                os.system('start ' + file)
            elif sysstr == 'Linux':
                os.system('xdg-open ' + file)

    def DeleteTabPanelButton(self, panel):
        end_one = len(panel.Buttons) - 1
        for i in range(0, len(panel.Buttons) - 1, 1):
            if panel.Buttons[i].isEnabled() is False:
                panel.Buttons[i].deleteLater()
                panel.Buttons.remove(panel.Buttons[i])
            animation = QtCore.QPropertyAnimation(self)
            animation.setDuration(150)
            animation.setPropertyName(b'pos')
            animation.setTargetObject(panel.Buttons[i])
            animation.setStartValue(panel.Buttons[i].pos())
            r = i // 11
            w = i % 11
            animation.setEndValue(QtCore.QPoint(panel.GrimBox[w], panel.GrimBox[r]))
            animation.start()
        try:
            if panel.Buttons[end_one].isEnabled() is False:
                panel.Buttons[end_one].deleteLater()
                panel.Buttons.remove(panel.Buttons[end_one])
        except:
            pass
        i = len(panel.Buttons)
        animation = QtCore.QPropertyAnimation(self)
        animation.setDuration(150)
        animation.setPropertyName(b'pos')
        animation.setTargetObject(panel.TheAddButton)
        animation.setStartValue(panel.TheAddButton.pos())
        r = i // 11
        w = i % 11
        animation.setEndValue(QtCore.QPoint(panel.GrimBox[w], panel.GrimBox[r]))
        animation.start()

    def DeletePanel(self, panel):
        self.TabStack.removeWidget(panel)
        self.TabPanels.remove(panel)
        end_one = len(self.TabButtons) - 1
        for i in range(0, len(self.TabButtons) - 1, 1):
            if self.TabButtons[i].isEnabled() is False:
                self.TabButtons[i].deleteLater()
                self.TabButtons.remove(self.TabButtons[i])
            animation = QtCore.QPropertyAnimation(self)
            animation.setDuration(150)
            animation.setPropertyName(b'pos')
            animation.setTargetObject(self.TabButtons[i])
            animation.setStartValue(self.TabButtons[i].pos())
            r = i // 11
            w = i % 11
            animation.setEndValue(QtCore.QPoint(self.TabAreaPanel.GrimBox[w], self.TabAreaPanel.GrimBox[r]))
            animation.start()
        try:
            if self.TabButtons[end_one].isEnabled() is False:
                self.TabButtons[end_one].deleteLater()
                self.TabButtons.remove(self.TabButtons[end_one])
        except:
            pass
        i = len(self.TabButtons)
        animation = QtCore.QPropertyAnimation(self)
        animation.setDuration(150)
        animation.setPropertyName(b'pos')
        animation.setTargetObject(self.TabAreaPanel.TheAddButton)
        animation.setStartValue(self.TabAreaPanel.TheAddButton.pos())
        r = i // 11
        w = i % 11
        animation.setEndValue(QtCore.QPoint(self.TabAreaPanel.GrimBox[w], self.TabAreaPanel.GrimBox[r]))
        animation.start()


class ResizablePanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ResizablePanel, self).__init__(parent)
        self.r = 0
        self.TheAddButton = uni_Widget.ICTFEButton(self)
        self.TheAddButton.setGeometry(QtCore.QRect(0, 0, 128, 128))
        self.TheAddButton.setObjectName('TheAddButton')
        font = QtGui.QFont()
        font.setFamily('文泉驿微米黑')
        font.setPixelSize(50)
        self.TheAddButton.setText('+')
        self.TheAddButton.setFont(font)
        self.Buttons = []
        self.GrimBox = [0, 128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280]

    def addButton(self, text):
        button = DIYedButton(self)
        self.Buttons.append(button)
        button.setObjectName(text)
        button.setText(text)
        button.show()
        i = len(self.Buttons) - 1
        button.setGeometry(QtCore.QRect(self.GrimBox[i % 11], self.GrimBox[i // 11], 128, 128))
        i += 1
        animation = QtCore.QPropertyAnimation(self)
        animation.setTargetObject(self.TheAddButton)
        animation.setPropertyName(b'pos')
        animation.setDuration(150)
        animation.setStartValue(self.TheAddButton.pos())
        animation.setEndValue(QtCore.QPoint(self.GrimBox[i % 11], self.GrimBox[i // 11]))
        animation.start()
        if i // 11 > self.r:
            self.r = i // 11
            self.resize(1426, self.GrimBox[self.r + 1])
        return button


class DIYedButton(uni_Widget.ICTFEButton):
    Deleted = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(DIYedButton, self).__init__(parent)

    def contextMenuEvent(self, event):
        menu = QtWidgets.QMenu(self)
        quit_action = menu.addAction("删除")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == quit_action:
            self.setEnabled(False)
            self.Deleted.emit()
