from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui_Widgets import uni_Widget


class DragList(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # init
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)
        self.headerItem().setText(0, "模块")


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
                    pass
            else:
                item.setHidden(True)
            cursor = cursor.__iadd__(1)

    def addDIYItem(self, name, categlories):
        # can be (icon, text, parent, <int>type)
        try:
            i = self.findItems(categlories, Qt.MatchStartsWith, column=0)[0]
        except:
            fa = QTreeWidgetItem(self)
            fa.setText(0, categlories)
            i = fa
        item = QTreeWidgetItem(i)
        item.setText(0, name)

        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable |
                      Qt.ItemIsDragEnabled)

    def startDrag(self, *args, **kwargs):

        item = self.currentItem()

        mimeData = QMimeData()
        mimeData.setText(item.text(0))

        drag = QDrag(self)
        drag.setMimeData(mimeData)

        drag.exec_(Qt.MoveAction)
