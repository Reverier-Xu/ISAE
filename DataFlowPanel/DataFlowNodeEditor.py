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
            node = self.scene.create_node(self.scene._registry.create(event_data))
            pos_view = self.mapToScene(event.pos())
            node.graphics_object.setPos(pos_view)
            self._scene.node_placed.emit(node)
        except:
            traceback.print_exc()
            super().dropEvent(event)
        super(CryptoFlowView, self).dropEvent(event)

    def dragEnterEvent(self, event: QDragEnterEvent):
        event.acceptProposedAction()
        super(CryptoFlowView, self).dragEnterEvent(event)

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
