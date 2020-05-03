__AUTHOR__ = 'Reverier Xu'

from PyQt5 import QtWidgets, QtCore, QtGui
from ui_Widgets import uni_Widget
from ui_Widgets.qtpynodeeditor import Node


class OptionsEditBox(QtWidgets.QTableWidget):
    settings = {}
    properties = {}
    node = None

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setColumnCount(2)
        self.horizontalHeader().setStretchLastSection(True)
        font = QtGui.QFont()
        font.setFamily('文泉驿微米黑')
        font.setPixelSize(20)
        self.setFont(font)
        self.horizontalHeader().hide()
        self.verticalHeader().hide()
        self.setStyleSheet("QTableWidget{"
                           "background-color: transparent;"
                           "border:1px solid rgb(50, 50, 50)"
                           "}"
                           "QTableWidget::item{"
                           "border:1px solid rgb(50, 50, 50)"
                           "}")

    def LoadOptions(self, node: Node):
        self.setRowCount(0)
        try:
            prop = node.model.properties
            settings = node.model.settings
            self.settings = settings
            self.properties = prop
            self.node = node
        except AttributeError:
            return
        rows = len(prop['properties'])
        self.setRowCount(rows)
        k = 0
        for i in prop['properties']:
            name_item = QtWidgets.QTableWidgetItem(i)
            name_item.setFlags(QtCore.Qt.ItemIsEditable)
            self.setItem(k, 0, name_item)
            if prop['properties'][i] == bool:
                exec_item = uni_Widget.ICTFECheckBox()
                exec_item.setText('True')
                exec_item.stateChanged.connect(self.GetOptions)
                exec_item.setChecked(settings[i])
            elif prop['properties'][i] == str:
                exec_item = uni_Widget.ICTFELineBox()
                exec_item.setStyleSheet('color: white;'
                                        'border: 0px solid gray;'
                                        'border-radius: 0px;'
                                        'padding: 0 4px;'
                                        'background: rgb(30, 30, 30);'
                                        'selection-background-color: blue;')
                exec_item.textEdited.connect(self.GetOptions)
                exec_item.setText(settings[i])
            elif type(prop['properties'][i]) == list:
                exec_item = QtWidgets.QComboBox()
                font = QtGui.QFont()
                font.setFamily('文泉驿微米黑')
                font.setPixelSize(20)
                exec_item.setFont(font)
                exec_item.setStyleSheet('border:0px solid rgb(50, 50, 50); color: white; background-color: rgb(30,30,30)')
                for j in prop['properties'][i]:
                    exec_item.addItem(j)
                exec_item.currentTextChanged.connect(lambda a: self.GetOptions())
                exec_item.setCurrentText(settings[i])
            else:
                continue
            self.setCellWidget(k, 1, exec_item)
            k += 1

    def GetOptions(self):
        try:
            rows = self.rowCount()
            for i in range(rows):
                if self.properties['properties'][self.item(i, 0).text()] == bool:
                    self.settings[self.item(i, 0).text()] = self.cellWidget(i, 1).isChecked()
                elif self.properties['properties'][self.item(i, 0).text()] == str:
                    self.settings[self.item(i, 0).text()] = self.cellWidget(i, 1).text()
                elif type(self.properties['properties'][self.item(i, 0).text()]) == list:
                    self.settings[self.item(i, 0).text()] = self.cellWidget(i, 1).currentText()
            return self.settings
        except AttributeError:
            pass
