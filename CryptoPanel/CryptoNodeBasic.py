import importlib
import os
from copy import copy

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui_Widgets.qtpynodeeditor import *
from PyQt5 import QtCore
import CryptoPanel.Modules
import pkgutil
import sys
from ui_Widgets import uni_Widget
from CryptoPanel.OptionEditBox import OptionsEditBox

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


for module in get_modules('CryptoPanel/Modules'):
    module = importlib.import_module(module, 'CryptoPanel.Modules')
    try:
        Modules[module.properties['name']] = module
    except:
        pass


class StringData(NodeData):
    data_type = NodeDataType(id='string', name='str')

    def __init__(self, string: str):
        super().__init__()
        self.string = string


class InputModel(NodeDataModel):
    name = 'Input'
    caption = 'Input'
    caption_visible = True
    port_caption_visible = True
    num_ports = {PortType.input: 0,
                 PortType.output: 1,
                 }
    port_caption = {
        'input': {

        },
        'output': {
            0: '输出'
        }
    }
    data_type = StringData

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._string = None
        self._edit = uni_Widget.ICTFETextBox()
        self._edit.textChanged.connect(self.onTextEdited)

    def resizable(self):
        return True

    def out_data(self, port):
        return StringData(self._string)

    def embedded_widget(self):
        return self._edit

    def onTextEdited(self, **kwargs):
        self._string = self._edit.toPlainText()
        self.data_updated.emit(0)


class OutputModel(NodeDataModel):
    name = 'Output'
    caption = 'Output'
    caption_visible = True
    port_caption_visible = True
    num_ports = {PortType.input: 1,
                 PortType.output: 1,
                 }
    port_caption = {
        'input': {
            0: '输入'
        },
        'output': {
            0: '中继'
        }
    }
    data_type = StringData

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._node_data = None
        self._show = uni_Widget.ICTFETextBox()
        self._show.setReadOnly(True)
        self._show.setText('未连接..')

    def resizable(self):
        return True

    def set_in_data(self, node_data, port):
        self._node_data = node_data
        if (self._node_data and
                self._node_data.data_type == StringData.data_type and
                self._node_data.string):
            string = node_data.string
        else:
            string = '未连接/未初始化.'

        self._show.setText(str(string))
        self.data_updated.emit(0)

    def out_data(self, port):
        return self._node_data

    def embedded_widget(self):
        return self._show


class CryptoComputeModel(NodeDataModel):
    caption_visible = True
    properties = None
    port_caption_visible = True
    data_type = StringData.data_type
    computed = False

    def __init__(self, module, *args, **kwargs):

        super().__init__(*args, **kwargs)

    @property
    def caption(self):
        return self.name

    def out_data(self, port: int) -> NodeData:
        '''
        The output data as a result of this calculation

        Parameters
        ----------
        port : int

        Returns
        -------
        value : NodeData
        '''
        try:
            return copy(self.outputs[port])
        except:
            return None

    def set_in_data(self, data: NodeData, port: Port):
        '''
        New data at the input of the node

        Parameters
        ----------
        data : NodeData
        port_index : int
        '''
        self.inputs[port.index] = copy(data)
        if self._check_inputs():
            try:
                self.compute()
                self.data_updated.emit(0)
            except:
                pass
        else:
            for i in self.outputs:
                self.outputs[i] = None
            self.data_updated.emit(0)
        self.computed = False

    def _check_inputs(self):
        try:
            for i in self.inputs:
                if self.inputs[i].data_type != StringData.data_type:
                    return False
            return True
        except:
            return False

    def compute(self):
        if self.computed:
            pass
        inp = {}
        for i in self.inputs:
            inp[i] = self.inputs[i].string
        print(self, self.settings, id(self.settings))
        out = self.func(inp, self.settings)
        for i in out:
            self.outputs[i] = StringData(out[i])
        self.computed = True


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
        eventData = event.mimeData().text()

        node = self.scene.create_node(self.scene._registry.create(eventData))
        pos_view = self.mapToScene(event.pos())
        node.graphics_object.setPos(pos_view)
        self._scene.node_placed.emit(node)

    def dragEnterEvent(self, event: QDragEnterEvent):
        event.acceptProposedAction()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete and event.modifiers() & Qt.ControlModifier:
            self.delete_selected()
        else:
            super().keyPressEvent(event)


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
