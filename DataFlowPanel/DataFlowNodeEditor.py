__AUTHOR__ = 'Reverier Xu'

from DataFlowPanel.DataFlowNodeModel import *



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
