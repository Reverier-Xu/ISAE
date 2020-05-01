from DataFlowPanel.DataFlowNodeModel import *

import importlib
import os

Modules = {}


def get_modules(package="."):
    """
    获取包名下所有非__init__的模块名
    """
    modules = []
    files = os.listdir(package)

    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)
            modules.append("." + name)

    return modules


for module in get_modules('Modules/DataFlow'):
    module = importlib.import_module(module, 'Modules.DataFlow')
    try:
        Modules[module.properties['name']] = module
    except:
        pass


class CryptoFlowView(FlowView):
    settingsMap = {}

    def __init__(self, scene, parent=None):
        super().__init__(scene, parent=parent)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setAcceptDrops(True)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def dropEvent(self, event: QDropEvent):
        event_data = event.mimeData().text()
        try:
            node = self.scene.create_node(
                self.scene._registry.create(event_data))
            pos_view = self.mapToScene(event.pos())
            node.graphics_object.setPos(pos_view)
            self._scene.node_placed.emit(node)
        except:
            traceback.print_exc()
            super().dropEvent(event)

    def dragEnterEvent(self, event: QDragEnterEvent):
        event.acceptProposedAction()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete and event.modifiers() & Qt.ControlModifier:
            self.delete_selected()
        else:
            super().keyPressEvent(event)

    def delete_selected(self):

        for item in self._scene.selectedItems():
            if isinstance(item, ConnectionGraphicsObject):
                self._scene.delete_connection(item.connection)

        if not self._scene.allow_node_deletion:
            return

        for item in self._scene.selectedItems():
            if isinstance(item, NodeGraphicsObject):
                try:
                    item.node.model.p.terminate()
                except:
                    pass
                self._scene.remove_node(item.node)


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
                           "QTreeWidget{color: lightgrey; background-color: rgb(20, 20, 20)}")
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
