from PyQt5.QtCore import QMimeData, QPoint, Qt
from PyQt5.QtGui import QDrag

from ui_Widgets import uni_Widget


class FileStack(uni_Widget.ICTFEList):
    def __init__(self, parent):
        super(FileStack, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.setDropAction(Qt.MoveAction)
        event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasFormat("text/plain"):
            data = event.mimeData().text()
            text = data
            self.addItem(text)
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def startDrag(self, dropActions, **kwargs):
        item = self.currentItem()
        mime_data = QMimeData()
        mime_data.setText(item.text())
        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.setHotSpot(QPoint(12, 12))
        drag.exec(Qt.MoveAction)
