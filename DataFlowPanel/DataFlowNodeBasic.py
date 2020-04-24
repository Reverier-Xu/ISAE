import importlib
import os
from copy import copy

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui_Widgets.qtpynodeeditor import *
from PyQt5 import QtCore
import DataFlowPanel.Modules
import pkgutil
import sys
from ui_Widgets import uni_Widget
from DataFlowPanel.OptionEditBox import OptionsEditBox
import traceback

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


for module in get_modules('DataFlowPanel/Modules'):
    module = importlib.import_module(module, 'DataFlowPanel.Modules')
    try:
        Modules[module.properties['name']] = module
    except:
        pass


class ComputeThread(QThread):
    func = None
    inp = None
    settings = None
    results = None

    def __init__(self, func, parent=None):
        super().__init__(parent=parent)
        self.func = func

    def run(self):
        try:
            self.results = self.func(self.inp, self.settings)
        except:
            self.results = None

    def getResult(self):
        return copy(self.results)

    def setData(self, inp, settings):
        self.inp = inp
        self.settings = settings


class StringData(NodeData):
    data_type = NodeDataType(id='string', name='data')

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


class FileInputModel(NodeDataModel):
    name = 'File Input'
    caption = 'File Input'
    num_ports = {PortType.input: 0,
                 PortType.output: 1,
                 }
    data_type = StringData.data_type

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = None
        self._label = uni_Widget.ICTFELabel()
        self._label.setText('点击选择文件')
        self._label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

        self._label.setFixedSize(200, 100)
        self._label.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj is not self._label:
            return False

        if event.type() == QtCore.QEvent.MouseButtonPress:
            file_name, _ = QFileDialog.getOpenFileName(
                None, "打开文件", QtCore.QDir.homePath(),
                "all(*)")
            try:
                with open(file_name, 'rb') as out:
                    self._data = out.read()
            except Exception as ex:
                print(f'Failed to load file {file_name}: {ex}')
                return False
            self._label.setText(file_name)
            self.data_updated.emit(0)
            return True

        return False

    def resizable(self):
        return True

    def out_data(self, port):
        return StringData(self._data)

    def embedded_widget(self):
        return self._label


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
        try:
            self._show.setText(string.decode())
        except:
            self._show.setText(str(string))
        self.data_updated.emit(0)

    def out_data(self, port):
        return self._node_data

    def embedded_widget(self):
        return self._show


class ImageShowModel(NodeDataModel):
    caption = 'Image Output'
    name = 'Image Output'
    num_ports = {PortType.input: 1,
                 PortType.output: 0,
                 }
    data_type = StringData

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._node_data = None
        self.pixmap = None
        self._label = QLabel('Image')
        self._label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

        self._label.setFixedSize(200, 200)
        self._label.installEventFilter(self)

    def resizable(self):
        return True

    def eventFilter(self, obj, event):
        if obj is self._label and event.type() == QtCore.QEvent.Resize:
            if (self._node_data and
                    self._node_data.data_type == StringData.data_type and
                    self._node_data.string):
                w, h = self._label.width(), self._label.height()
                try:
                    self._label.setPixmap(self.pixmap.scaled(w, h, Qt.KeepAspectRatio))
                except:
                    pass

        return False

    def set_in_data(self, node_data, port):
        self._node_data = node_data
        try:
            if (self._node_data and
                    self._node_data.data_type == StringData.data_type and
                    self._node_data.string):
                w, h = self._label.width(), self._label.height()
                if type(node_data.string) == str and node_data.string[:2] == 'b\'':
                    inp = eval(node_data.string)
                else:
                    inp = node_data.string
                pixmap = QPixmap()
                pixmap.loadFromData(inp)
            else:
                pixmap = QPixmap()
            self._label.setPixmap(pixmap.scaled(w, h, Qt.KeepAspectRatio))
            self.pixmap = pixmap
        except:
            self._label.setText('Error.')
            self.pixmap = None

    def embedded_widget(self):
        return self._label


class CryptoComputeModel(NodeDataModel):
    caption_visible = True
    properties = None
    port_caption_visible = True
    data_type = StringData.data_type
    computeEndedSig = pyqtSignal()
    computeThread = None

    def __init__(self, module, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.computeEndedSig.connect(self._emit_results)
        self._statusLabel = uni_Widget.ICTFELabel()
        self._statusLabel.setText('?')
        self._statusLabel.setMinimumWidth(20)
        self._statusLabel.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.computeThread = ComputeThread(self.func)
        self.computeThread.finished.connect(self._compute_callback)

    @property
    def caption(self):
        return self.name

    def embedded_widget(self):
        return self._statusLabel

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
            except Exception as e:
                traceback.print_exc()
        else:
            self._statusLabel.setText('×')
            for i in self.outputs:
                self.outputs[i] = None
            for i in range(self.num_ports[PortType.output]):
                self.data_updated.emit(i)

    def _emit_results(self):
        for i in range(self.num_ports[PortType.output]):
            self.data_updated.emit(i)

    def _check_inputs(self):
        try:
            for i in self.inputs:
                if self.inputs[i].data_type != StringData.data_type:
                    return False
            return True
        except:
            return False

    def compute(self):
        self._statusLabel.setText('...')
        inp = {}
        print(self.inputs[0].string)
        for i in self.inputs:
            try:
                inp[i] = self.inputs[i].string.decode()
            except:
                if self.inputs[i].string is not None:
                    inp[i] = str(self.inputs[i].string)
                else:
                    inp[i] = None
        if self.computeThread.isRunning():
            self.computeThread.quit()
            self.computeThread.wait()
        self.computeThread.setData(inp, self.settings)
        self.computeThread.start()

    def _compute_error_callback(self, error=None, *args, **kwargs):
        print(error)
        for i in self.outputs:
            self.outputs[i] = None
        for i in range(self.num_ports[PortType.output]):
            self.data_updated.emit(i)
        self._statusLabel.setText('×')

    def _compute_callback(self):
        out = self.computeThread.getResult()
        if out is None:
            self._compute_error_callback()
            return
        out = copy(out)
        for i in out:
            self.outputs[i] = StringData(out[i])
        self.computeEndedSig.emit()
        self._statusLabel.setText('√')


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
        try:
            node = self.scene.create_node(
                self.scene._registry.create(eventData))
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
        # Delete the selected connections first, ensuring that they won't be
        # automatically deleted when selected nodes are deleted (deleting a node
        # deletes some connections as well)
        for item in self._scene.selectedItems():
            if isinstance(item, ConnectionGraphicsObject):
                self._scene.delete_connection(item.connection)

        if not self._scene.allow_node_deletion:
            return

        # Delete the nodes; self will delete many of the connections.
        # Selected connections were already deleted prior to self loop, otherwise
        # qgraphicsitem_cast<NodeGraphicsObject*>(item) could be a use-after-free
        # when a selected connection is deleted by deleting the node.
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
                    pass
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

        mimeData = QMimeData()
        mimeData.setText(item.text(0))

        drag = QDrag(self)
        drag.setMimeData(mimeData)

        drag.exec_(Qt.MoveAction)
