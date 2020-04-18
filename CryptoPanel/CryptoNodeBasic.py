import importlib
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui_Widgets.nodeeditor.node_node import Node
from ui_Widgets.nodeeditor.node_content_widget import QDMNodeContentWidget
from ui_Widgets.nodeeditor.node_graphics_node import QDMGraphicsNode
from ui_Widgets.nodeeditor.node_socket import LEFT_CENTER, RIGHT_CENTER
from ui_Widgets.nodeeditor.utils import dumpException
from ui_Widgets import uni_Widget
from ui_Widgets.ErrorWin import errorInfo
from ui_Widgets.nodeeditor.node_editor_widget import NodeEditorWidget
from PyQt5 import QtCore
import CryptoPanel.Modules
import pkgutil
import sys


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


class CryptoGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 160
        self.height = 120
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()

class IOGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 300
        self.height = 200
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()

class CryptoNodeContent(QDMNodeContentWidget):
    def initUI(self):
        self.layouts = QVBoxLayout(self)
        lbl = uni_Widget.ICTFELabel(self.node.content_label)
        lbl.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        lbl.setObjectName(self.node.content_label_objname)
        self.layouts.addWidget(lbl)

class IONodeContent(QDMNodeContentWidget):
    def initUI(self):
        self.layouts = QVBoxLayout(self)
        self.textBox = uni_Widget.ICTFETextBox(self)
        self.textBox.setObjectName(self.node.content_label_objname)
        self.layouts.addWidget(self.textBox)


class CryptoNode(Node):
    icon = ""
    op_code = 0
    op_title = "CryptoNode"
    content_label = ""
    content_label_objname = "calc_node_bg"
    name = ''

    GraphicsNode_class = CryptoGraphicsNode
    NodeContent_class = CryptoNodeContent

    def __init__(self, scene, properties: dict = None):
        self.prop = properties
        inputs = []
        outputs = []
        self.content_label = properties['name']
        self.name = properties['name']
        for i in range(properties['input']):
            inputs.append(2)
        for i in range(properties['output']):
            outputs.append(1)
        super().__init__(scene, self.op_title, inputs, outputs)

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

class InputNode(Node):
    op_code = 1
    op_title = "Input"
    content_label_objname = "calc_node_input"

    def __init__(self, scene):
        super().__init__(scene, self.op_title, inputs=[], outputs=[1])

    def initInnerClasses(self):
        self.content = IONodeContent(self)
        self.grNode = IOGraphicsNode(self)

class OutputNode(Node):
    op_code = 2
    op_title = "Output"
    content_label_objname = "calc_node_output"

    def __init__(self, scene):
        super().__init__(scene, self.op_title, inputs=[2], outputs=[])

    def initInnerClasses(self):
        self.content = IONodeContent(self)
        self.grNode = IOGraphicsNode(self)


class Graph:
    ''' Input nodes '''
    inputs = []
    inputnodes={}

    ''' Output nodes '''
    outputs = []
    outputnodes={}

    ''' Nodes Properties: Node's ID -> Node's Properties(dict) '''
    properties = {}

    ''' Nodes' Maps: Node's ID -> dict('input' -> {Port -> [Node's ID, Port]}, 'output' -> {Port -> [[Node's ID, Port], [Node's ID, Port]]}) '''
    NodesMaps = {}

    ''' Node's Crypto Type: Node's ID -> CryptoFunc(object) '''
    NodeFunc = {}

    ''' Node's Status: Node's ID -> isComputed(bool)  '''
    NodeStatus = {}

    ''' Node's Result: Node's ID -> Result(dict: properties) '''
    NodeResults = {}

    def RegisterNode(self, node: Node):
        dic = node.serialize()
        if node.op_code == 1:
            self.inputs.append(dic['id'])
            self.inputnodes[dic['id']] = node
            self.properties[dic['id']] = {'input': {}, 'output': {}}
            self.NodeStatus[dic['id']] = False
            self.NodesMaps[dic['id']] = {'input': {}, 'output': {}}
            self.NodeResults[dic['id']] = {'input': {}, 'output': {}}
            self.NodeFunc[dic['id']] = None
        elif node.op_code == 2:
            self.outputs.append(dic['id'])
            self.properties[dic['id']] = {'input': {}, 'output': {}}
            self.outputnodes[dic['id']] = node
            self.NodeStatus[dic['id']] = False
            self.NodesMaps[dic['id']] = {'input': {}, 'output': {}}
            self.NodeResults[dic['id']] = {'input': {}, 'output': {}}
            self.NodeFunc[dic['id']] = None
        else:
            self.properties[dic['id']] = Modules[node.name].default
            self.NodeStatus[dic['id']] = False
            self.NodesMaps[dic['id']] = {'input': {}, 'output': {}}
            self.NodeResults[dic['id']] = {'input': {}, 'output': {}}
            self.NodeFunc[dic['id']] = Modules[node.name]

    def ConnectNode(self, edge: 'Edge'):
        starter = edge.start_socket.node
        starterPort = edge.start_socket.index
        ender = edge.end_socket.node
        enderPort = edge.end_socket.index
        starterData = starter.serialize()
        enderData = ender.serialize()
        if len(self.NodesMaps[starterData['id']]['output']) == 0:
            self.NodesMaps[starterData['id']]['output'][starterPort] = [[
                enderData['id'], enderPort]]
        else:
            self.NodesMaps[starterData['id']]['output'][starterPort].append([
                enderData['id'], enderPort])
        self.NodesMaps[enderData['id']]['input'][enderPort] = [
            starterData['id'], starterPort]

    def NodeDelete(self, dic:'OrderedDict'):
        id = dic['id']
        for i in self.inputs:
            if i == id:
                self.inputs.remove(id)
                self.inputnodes.pop(id)
        for i in self.outputs:
            if i == id:
                self.outputs.remove(id)
                self.outputnodes.pop(id)
        self.properties.pop(id)
        self.NodeStatus.pop(id)
        self.NodeFunc.pop(id)
        self.NodeResults.pop(id)
        clears = self.NodesMaps[id]
        for i in clears['input']:
            for j in self.NodesMaps[clears['input'][i][0]]['output']:
                for k in self.NodesMaps[clears['input'][i][0]]['output'][j]:
                    if k[0] == id:
                        self.NodesMaps[clears['input'][i][0]]['output'][j].remove(k)
                        break
        for i in clears['output']:
            for j in clears['output'][i]:
                for k in self.NodesMaps[j[0]]['input']:
                    if self.NodesMaps[j[0]]['input'][k][0] == id:
                        self.NodesMaps[j[0]]['input'].pop(k)
        self.NodesMaps.pop(id)
        print('After Delete the Node, the map is: ', self.NodesMaps)
        print('')

    def EdgeDelete(self, dic: dict):
        starterData = dic['starter'].serialize()
        enderData = dic['ender'].serialize()
        self.NodesMaps[starterData['id']]['output'][dic['starterPort']].remove([enderData['id'], dic['enderPort']])
        self.NodesMaps[enderData['id']]['input'].pop(dic['enderPort'])
        print('After Edge Deleted: ', self.NodesMaps)
        print('')

    def Compute(self):
        self.Modified()
        print('Before Computing, The Map is: ', self.NodesMaps)
        print('')
        print('The Data is: ', self.NodeResults)
        print('')
        print('The Node Properties is: ', self.properties)
        print('')
        for i in self.outputs:
            self.Get(i)
        print('After Computing, The Map is: ', self.NodesMaps)
        print('')
        print('The Data is: ', self.NodeResults)
        print('')
        print('The Node Properties is: ', self.properties)
        print('')

    def Get(self, id):
        if self.inputs.count(id) != 0:
            self.NodeResults[id]['output'][0] = self.inputnodes[id].content.textBox.toPlainText()
            self.NodeStatus[id] = True
            return True
        if self.NodeStatus[id]:
            return True
        for i in self.NodesMaps[id]['input']:
            ok = self.Get(self.NodesMaps[id]['input'][i][0])
            if not ok:
                return False
            # print(self.properties)
            self.properties[id]['input'][i] = self.NodeResults[
                self.NodesMaps[id]['input'][i][0]]['output'][self.NodesMaps[id]['input'][i][1]]
        if self.outputs.count(id) != 0:
            self.NodeResults[id] = self.properties[id]
            # print(id)
            try:
                self.outputnodes[id].content.textBox.setText(self.NodeResults[id]['input'][0])
            except:
                self.outputnodes[id].content.textBox.setText('Error!')
            self.NodeStatus[id] = True
            return True
        try:
            self.NodeResults[id] = self.NodeFunc[id].main(self.properties[id])
            self.NodeStatus[id] = True
            return True
        except:
            errorInfo(self, '出现错误, 请检查合法性!')
            return False

    def Modified(self):
        for i in self.NodeStatus:
            self.NodeStatus[i] = False
        for i in self.NodeResults:
            self.NodeResults[i] = {'input': {}, 'output': {}}
        for i in self.properties:
            self.properties[i]['input'] = {}
            self.properties[i]['output'] = {}


class CryptoNodeEditorWidget(NodeEditorWidget):
    graph = Graph()
    def __init__(self):
        super().__init__()
        # self.setAttribute(Qt.WA_DeleteOnClose)

        self.scene.addDragEnterListener(self.onDragEnter)
        self.scene.addDropListener(self.onDrop)

    def setTitle(self):
        self.setWindowTitle(self.getUserFriendlyFilename())

    def addCloseEventListener(self, callback):
        self._close_event_listeners.append(callback)

    def closeEvent(self, event):
        for callback in self._close_event_listeners:
            callback(self, event)

    def onDragEnter(self, event):
        event.acceptProposedAction()

    def onDrop(self, event):
        if event.mimeData().hasText():
            eventData = event.mimeData().text()
            text = eventData

            mouse_position = event.pos()
            scene_position = self.scene.grScene.views()[0].mapToScene(mouse_position)
            try:
                if text == 'input':
                    node = InputNode(self.scene)
                elif text == 'output':
                    node = OutputNode(self.scene)
                else:
                    node = CryptoNode(self.scene, Modules[text].properties)
                self.graph.RegisterNode(node)
                node.setPos(scene_position.x(), scene_position.y())
                self.scene.history.storeHistory(
                    "Created node %s" % node.__class__.__name__)
            except Exception as e:
                dumpException(e)

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            # print(" ... drop ignored, not requested format '%s'" % LISTBOX_MIMETYPE)
            event.ignore()
