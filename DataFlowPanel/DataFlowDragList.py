__AUTHOR__ = 'Reverier Xu'

import traceback

from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QFont
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidgetItemIterator, QAbstractItemView, QTreeWidget


class DragList(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # init
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)
        self.setStyleSheet("QTreeWidget::item:hover{color: lightgrey; background-color: rgb(60,150,225)}"
                           "QTreeWidget::item:selected{color: lightgrey; background-color:rgb(80,130,255)}"
                           "QTreeWidget{color: lightgrey; background-color: rgb(30, 30, 30)}")
        self.headerItem().setText(0, "模块")
        self.header().setVisible(False)
        font = QFont()
        font.setFamily('文泉驿微米黑')
        font.setPixelSize(24)
        self.setFont(font)

    def filter(self, text):
        """以text开头作为过滤条件示例"""
        cursor = QTreeWidgetItemIterator(self)
        while cursor.value():
            item = cursor.value()
            if item.text(0).startswith(text):
                item.setHidden(False)
                # 需要让父节点也显示,不然子节点显示不出来
                try:
                    item.parent().setHidden(False)
                except Exception:
                    traceback.print_exc()
            else:
                item.setHidden(True)
            cursor = cursor.__iadd__(1)

    def addDIYItem(self, name, categories):
        # can be (icon, text, parent, <int>type)
        try:
            i = self.findItems(categories, Qt.MatchStartsWith, column=0)[0]
        except:
            fa = QTreeWidgetItem(self)
            fa.setText(0, categories)
            i = fa
        item = QTreeWidgetItem(i)
        item.setText(0, name)

        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable |
                      Qt.ItemIsDragEnabled)

    def startDrag(self, *args, **kwargs):

        item = self.currentItem()

        mime_data = QMimeData()
        mime_data.setText(item.text(0))

        drag = QDrag(self)
        drag.setMimeData(mime_data)

        drag.exec_(Qt.MoveAction)
