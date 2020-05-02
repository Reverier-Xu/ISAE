from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

from Config import Settings
from ui_Widgets import uni_Widget
import os
import platform
import sqlite3
import subprocess
from ui_Widgets.ErrorWin import errorInfo


def OpenFile(file):
    try:
        subprocess.Popen(file)
    except:
        sysstr = platform.system()
        if sysstr == 'Windows':
            os.system('start \'' + file + '\'')
        elif sysstr == 'Linux':
            os.system('xdg-open \'' + file + '\'')


class ui_DIYPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ui_DIYPanel, self).__init__(parent, flags=Qt.WindowFlags())
        self.verticalLayout = QtWidgets.QVBoxLayout(self)

        self.verticalLayout.setObjectName("verticalLayout")
        self.TabAreaScroll = uni_Widget.ICTFEScrollArea(self)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.TabAreaScroll.sizePolicy().hasHeightForWidth())
        self.TabAreaScroll.setSizePolicy(size_policy)
        self.TabAreaScroll.setMinimumSize(QtCore.QSize(1200, 130))
        self.TabAreaScroll.setWidgetResizable(True)
        self.TabAreaScroll.setObjectName("TabAreaScroll")

        self.TabAreaPanel = ResizablePanel()
        self.TabAreaPanel.setGeometry(QtCore.QRect(0, 0, 1600, 128))
        self.TabAreaPanel.setObjectName("TabAreaPanel")
        self.TabAreaPanel.TheAddButton.clicked.connect(self.AddTabPanel)

        self.TabAreaPanel.setStyleSheet('background-color: transparent')
        self.TabAreaScroll.setWidget(self.TabAreaPanel)
        self.verticalLayout.addWidget(self.TabAreaScroll, alignment=Qt.Alignment())

        self.SplitterWidget = QtWidgets.QWidget(self, flags=Qt.WindowFlags())
        self.SplitterWidget.setMaximumHeight(1)
        self.SplitterWidget.setMinimumHeight(1)
        self.SplitterWidget.setStyleSheet("QWidget{"
                                          "background-color: grey;"
                                          "border: 1px grey;"
                                          "border-style: solid;"
                                          "}")
        self.verticalLayout.addWidget(self.SplitterWidget, alignment=Qt.Alignment())
        # 下层
        self.TabStack = QtWidgets.QStackedWidget(self)
        self.TabStack.setObjectName("TabStack")
        self.verticalLayout.addWidget(self.TabStack, alignment=Qt.Alignment())

        # 统一管理
        self.TabButtons = self.TabAreaPanel.Buttons  # 通过List进行有序化管理
        self.TabPanels = []
        self.FileButtons = []

        self.ReadDataBase()

    def ChangeTab(self, button, panel):
        self.TabStack.setCurrentWidget(panel)
        for i in self.TabButtons:
            i.setStyleSheet("QPushButton{"
                            "background-color:rgba(80, 160, 255, 80%);"
                            "color: white;"
                            "border-radius: 0px;"
                            "border: 0px groove gray;"
                            "border-style: outset;"
                            "}"
                            "QPushButton:hover{"
                            "background-color: rgba(80, 160, 80, 80%);"
                            "color: white;"
                            "}"
                            "QPushButton:pressed{"
                            "background-color: rgb(100, 100, 100);"
                            "border-style: inset; "
                            "}")
        button.setStyleSheet("QPushButton{"
                             "background-color:rgba(80, 255, 100, 80%);"
                             "color: white;"
                             "border-radius: 0px;"
                             "border: 0px groove gray;"
                             "border-style: outset;"
                             "}"
                             "QPushButton:hover{"
                             "background-color: rgba(80, 250, 180, 80%);"
                             "color: white;"
                             "}"
                             "QPushButton:pressed{"
                             "background-color: rgb(100, 100, 100);"
                             "border-style: inset; "
                             "}")

    def EditButtonName(self, panel, button):
        text = button.text()
        conn = sqlite3.connect('./Resources/DIY.sqlite')
        cu = conn.cursor()
        cu.execute('select FILEPATH from \'' + panel.objectName() +
                   '\' where BTNNAME=\'' + text + '\'')
        file = cu.fetchall()[0][0]
        new_name, ok = QtWidgets.QInputDialog.getText(self, '更改名称', '名称', flags=Qt.WindowFlags())
        if ok:
            button.setText(new_name)
            cu.execute(
                'update \'' + panel.objectName() + '\' set BTNNAME=\'' + new_name + '\' where FILEPATH=\'' + file + '\'')
            conn.commit()
            conn.close()

    def ReadDataBase(self):
        conn = sqlite3.connect('./Resources/DIY.sqlite')
        cu = conn.cursor()
        cu.execute("select name from sqlite_master where type='table'")
        tab_name = cu.fetchall()
        tab_name = [line[0] for line in tab_name]
        conn.commit()
        for i in tab_name:
            panel = self.AddTabPanelFile(i)
            cu.execute('select * from \'' + i + '\'')
            btn_list = cu.fetchall()
            conn.commit()
            for j in btn_list:
                self.AddTabPanelButtonFile(panel, j[1], j[0])
        conn.close()

    def AddTabPanel(self):
        text, ok = QtWidgets.QInputDialog.getText(self, '创建分区', '名称')
        for i in self.TabPanels:
            if text == i.objectName():
                errorInfo(self, '不能创建两个相同的分区!')
                return
        if ok:
            button = self.TabAreaPanel.addButton(text)
            panel = ResizablePanel()
            panel.setObjectName(text)
            self.TabStack.addWidget(panel)
            self.TabPanels.append(panel)
            button.clicked.connect(
                lambda: self.ChangeTab(button, panel))
            button.Deleted.connect(lambda: self.DeletePanel(panel))
            panel.TheAddButton.clicked.connect(
                lambda: self.AddTabPanelButton(panel))
            panel.DropFileSignal.connect(
                lambda s: self.AddTabPanelButtonDrop(s, panel))
            self.FileButtons.append(panel.Buttons)
            conn = sqlite3.connect('./Resources/DIY.sqlite')
            cu = conn.cursor()
            cu.execute('CREATE TABLE \'' + text +
                       '\' (BTNNAME TEXT, FILEPATH TEXT );')
            conn.commit()
            conn.close()

    def AddTabPanelFile(self, text):
        button = self.TabAreaPanel.addButton(text)
        panel = ResizablePanel()
        panel.setObjectName(text)
        self.TabStack.addWidget(panel)
        self.TabPanels.append(panel)
        button.clicked.connect(lambda: self.ChangeTab(button, panel))
        button.Deleted.connect(lambda: self.DeletePanel(panel))
        panel.TheAddButton.clicked.connect(
            lambda: self.AddTabPanelButton(panel))
        panel.DropFileSignal.connect(
            lambda s: self.AddTabPanelButtonDrop(s, panel))
        self.FileButtons.append(panel.Buttons)
        return panel

    def AddTabPanelButton(self, panel):
        file, ok = QtWidgets.QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         Settings.GlobalPath,
                                                         "All Files (*)")
        if ok:
            name, ok = QtWidgets.QInputDialog.getText(self, '创建启动按钮', '名称')
            conn = sqlite3.connect('./Resources/DIY.sqlite')
            cu = conn.cursor()
            try:
                cu.execute(
                    'INSERT INTO \'' + panel.objectName() + '\' (BTNNAME, FILEPATH) VALUES (\'' + name + '\',\'' + file + '\')')
                conn.commit()
            except:
                errorInfo('添加失败!\n请检查是否有重复项!')
            conn.close()
            button = panel.addButton(name)
            button.clicked.connect(lambda: OpenFile(file))
            button.Deleted.connect(lambda: self.DeleteTabPanelButton(panel))
            button.EditNameSignal.connect(
                lambda: self.EditButtonName(panel, button))

    def AddTabPanelButtonDrop(self, path, panel):
        ogrinfo = platform.system()
        if ogrinfo == 'Windows':
            split_chr = '\\'
        else:
            split_chr = '/'
        name = path.split(split_chr)[-1]
        self.AddTabPanelButtonFile(panel, path, name)
        conn = sqlite3.connect('./Resources/DIY.sqlite')
        cu = conn.cursor()
        try:
            cu.execute(
                'INSERT INTO \'' + panel.objectName() + '\' (BTNNAME, FILEPATH) VALUES (\'' + name + '\',\'' + path + '\')')
            conn.commit()
        except:
            errorInfo(self, '添加失败!\n请检查是否有重复项!')
        conn.close()

    def AddTabPanelButtonFile(self, panel, file, name):
        button = panel.addButton(name)
        button.clicked.connect(lambda: OpenFile(file))
        button.Deleted.connect(lambda: self.DeleteTabPanelButton(panel))
        button.EditNameSignal.connect(
            lambda: self.EditButtonName(panel, button))

    def DeleteTabPanelButton(self, panel):
        end_one = len(panel.Buttons) - 1
        aim_btn = ''
        for i in range(0, len(panel.Buttons) - 1, 1):
            if panel.Buttons[i].isEnabled() is False:
                aim_btn = panel.Buttons[i].text()
                panel.Buttons[i].deleteLater()
                panel.Buttons.remove(panel.Buttons[i])
            animation = QtCore.QPropertyAnimation(self)
            animation.setDuration(150)
            animation.setPropertyName(b'pos')
            animation.setTargetObject(panel.Buttons[i])
            animation.setStartValue(panel.Buttons[i].pos())
            r = i // 12
            w = i % 12
            animation.setEndValue(QtCore.QPoint(
                panel.GrimBox[w], panel.GrimBox[r]))
            animation.start()
        try:
            if panel.Buttons[end_one].isEnabled() is False:
                aim_btn = panel.Buttons[end_one].text()
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
        r = i // 12
        w = i % 12
        animation.setEndValue(QtCore.QPoint(
            panel.GrimBox[w], panel.GrimBox[r]))
        animation.start()
        if aim_btn != '':
            conn = sqlite3.connect('./Resources/DIY.sqlite')
            cu = conn.cursor()
            cu.execute('DELETE from \'' + panel.objectName() +
                       '\' where BTNNAME=\'' + aim_btn + '\';')
            conn.commit()
            conn.close()

    def DeletePanel(self, panel):
        conn = sqlite3.connect('./Resources/DIY.sqlite')
        cu = conn.cursor()
        cu.execute('DROP TABLE \'' + panel.objectName() + '\'')
        conn.commit()
        conn.close()
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
            r = i // 12
            w = i % 12
            animation.setEndValue(QtCore.QPoint(
                self.TabAreaPanel.GrimBox[w], self.TabAreaPanel.GrimBox[r]))
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
        r = i // 12
        w = i % 12
        animation.setEndValue(QtCore.QPoint(
            self.TabAreaPanel.GrimBox[w], self.TabAreaPanel.GrimBox[r]))
        animation.start()


class ResizablePanel(QtWidgets.QWidget):
    DropFileSignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(ResizablePanel, self).__init__(parent, flags=Qt.WindowFlags())
        self.setAcceptDrops(True)
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
        self.GrimBox = [0, 130, 260, 390, 520,
                        650, 780, 910, 1040, 1170, 1300, 1430]
        # self.GrimBox = [0, 128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280]

    def addButton(self, text):
        button = DIYedButton(self)
        self.Buttons.append(button)
        button.setObjectName(text)
        button.setText(text)
        button.show()
        i = len(self.Buttons) - 1
        button.setGeometry(QtCore.QRect(
            self.GrimBox[i % 12], self.GrimBox[i // 12], 128, 128))
        i += 1
        animation = QtCore.QPropertyAnimation(self)
        animation.setTargetObject(self.TheAddButton)
        animation.setPropertyName(b'pos')
        animation.setDuration(150)
        animation.setStartValue(self.TheAddButton.pos())
        animation.setEndValue(QtCore.QPoint(
            self.GrimBox[i % 12], self.GrimBox[i // 12]))
        animation.start()
        return button

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.LinkAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            # 遍历输出拖动进来的所有文件路径
            for url in event.mimeData().urls():
                path = url.toLocalFile()
                self.DropFileSignal.emit(path)
            event.acceptProposedAction()
        else:
            event.ignore()


class DIYedButton(QtWidgets.QPushButton):
    Deleted = QtCore.pyqtSignal()
    EditNameSignal = QtCore.pyqtSignal()
    EditCmdSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(DIYedButton, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPixelSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet(
            "QPushButton{"
            "background-color:rgba(80, 160, 255, 80%);"
            "color: white;"
            "border-radius: 0px;"
            "border: 0px groove gray;"
            "border-style: outset;"
            "}"
            "QPushButton:hover{"
            "background-color: rgba(80, 160, 80, 80%);"
            "color: white;"
            "}"
            "QPushButton:pressed{"
            "background-color: rgb(100, 100, 100);"
            "border-style: inset; "
            "}")

    def contextMenuEvent(self, event):
        menu = QtWidgets.QMenu(self)
        edit_name_action = menu.addAction("编辑名称")
        quit_action = menu.addAction("删除")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == quit_action:
            self.setEnabled(False)
            self.Deleted.emit()
        if action == edit_name_action:
            self.EditNameSignal.emit()
