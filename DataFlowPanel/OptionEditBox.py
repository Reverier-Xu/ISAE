from PyQt5 import QtWidgets, QtCore, QtGui
from ui_Widgets import uni_Widget


class OptionsEditBox(QtWidgets.QTableWidget):
    settings = {}
    properties = {}
    node = None
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setColumnCount(2)
        self.horizontalHeader().setStretchLastSection(True)
        font = QtGui.QFont()
        font.setFamily('文泉驿微米黑')
        font.setPixelSize(20)
        self.setFont(font)
        self.horizontalHeader().hide()
        self.verticalHeader().hide()
        self.setStyleSheet("QTableWidget{background-color: transparent;border:1px solid grey}"
                           "QTableWidget::item{border:1px solid grey}")


    def LoadOptions(self, node: 'Node'):
        self.setRowCount(0)
        try:
            prop = node.model.properties
            settings = node.model.settings
            self.settings = settings
            self.properties = prop
            self.node = node
        except:
            return
        rows = len(prop['properties'])
        self.setRowCount(rows)
        k = 0
        for i in prop['properties']:
            nameItem = QtWidgets.QTableWidgetItem(i)
            nameItem.setFlags(QtCore.Qt.ItemIsEditable)
            self.setItem(k, 0, nameItem)
            if prop['properties'][i] == bool:
                execItem = uni_Widget.ICTFECheckBox()
                execItem.setText('True')
                execItem.setChecked(settings[i])
            elif prop['properties'][i] == str:
                execItem = uni_Widget.ICTFELineBox()
                execItem.setStyleSheet('color: white;'
                                       'border: 0px solid gray;'
                                       'border-radius: 0px;'
                                       'padding: 0 4px;'
                                       'background: rgb(20, 20, 20);'
                                       'selection-background-color: blue;')
                execItem.setText(settings[i])
            elif type(prop['properties'][i]) == list:
                execItem = QtWidgets.QComboBox()
                font = QtGui.QFont()
                font.setFamily('文泉驿微米黑')
                font.setPixelSize(20)
                execItem.setFont(font)
                execItem.setStyleSheet('border:0px solid grey; color: white; background-color: rgb(30,30,30)')
                for j in prop['properties'][i]:
                    execItem.addItem(j)
                execItem.setCurrentText(settings[i])
            else:
                continue
            self.setCellWidget(k, 1, execItem)
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
        except:
            pass
