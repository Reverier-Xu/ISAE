import importlib
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui_Widgets.qtpynodeeditor import *
from PyQt5 import QtCore
import CryptoPanel.Modules
import pkgutil
import sys
from ui_Widgets import uni_Widget

Modules = {}
'''
CRYPTO_OP_CODE = 0
INPUT_OP_CODE = 1
OUTPUT_OP_CODE = 2
'''


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
    caption = 'Input'
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

    def resizable(self):
        return True

    def out_data(self, port):
        self._string = self._edit.toPlainText()
        return StringData(self._string)

    def embedded_widget(self):
        return self._edit


class ImageShowModel(NodeDataModel):
    caption = 'Output'
    num_ports = {PortType.input: 1,
                 PortType.output: 1,
                 }
    data_type = StringData

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._node_data = None
        self._show = uni_Widget.ICTFETextBox

    def resizable(self):
        return True

    def set_in_data(self, node_data, port):
        self._node_data = node_data
        if (self._node_data and
                self._node_data.data_type == StringData.data_type and
                self._node_data.string):
            string = node_data.string
        else:
            string = 'Error.'

        self._show.setText(string)
        self.data_updated.emit(0)

    def out_data(self, port):
        return self._node_data

    def embedded_widget(self):
        return self._show


class CryptoComputeModel(NodeDataModel):
    caption_visible = True
    name = 'CRYPTO'
    num_ports = {
        PortType.input: 2,
        PortType.output: 1,
    }
    port_caption = {'input': {0: '1', 1: '2'}, 'output': {0: '1'}}
    properties = None
    port_caption_visible = True
    data_type = StringData.data_type
    settings = None
    inputs = {}
    outputs = {}

    def __init__(self, module, *args, **kwargs):
        self.num_ports[PortType.input] = len(module.properties['input'])
        self.num_ports[PortType.output] = len(module.properties['output'])
        self.port_caption['input'] = module.properties['input']
        self.port_caption['output'] = module.properties['output']
        self.name = module.properties['name']
        self.properties = module.properties
        self.settings = module.defaults
        self.func = module.main
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
        return self.outputs[port]

    def set_in_data(self, data: NodeData, port: Port):
        '''
        New data at the input of the node

        Parameters
        ----------
        data : NodeData
        port_index : int
        '''
        self.inputs[port.index] = data

        if self._check_inputs():
            try:
                self.compute()
            except:
                pass

    def _check_inputs(self):
        try:
            for i in self.inputs:
                if self.inputs[i].data_type != StringData.data_type:
                    return False
            return True
        except:
            return False

    def compute(self):
        inp = {}
        for i in self.inputs:
            inp[i] = self.inputs[i].string
        out = self.func(inp, self.settings)
        for i in out:
            self.outputs[i] = StringData(out[i])


'''
class CryptoGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 200
        self.height = 300
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self.icons = QImage("Resources/status_icons.png")

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        super().paint(painter, QStyleOptionGraphicsItem, widget)

        offset = 24.0
        if self.node.isDirty():
            offset = 0.0
        if self.node.isInvalid():
            offset = 48.0

        painter.drawImage(
            QRectF(-10, -10, 24.0, 24.0),
            self.icons,
            QRectF(offset, 0, 24.0, 24.0)
        )


class CryptoContent(QDMNodeContentWidget):
    properties = {}
    settings = {}
    settingmap = {}

    def __init__(self, node: Node, parent: QWidget = None, properties: dict = None, settings: dict = None):
        """
        :param node: reference to the :py:class:`~nodeeditor.node_node.Node`
        :type node: :py:class:`~nodeeditor.node_node.Node`
        :param parent: parent widget
        :type parent: QWidget

        :Instance Attributes:
            - **node** - reference to the :class:`~nodeeditor.node_node.Node`
            - **layout** - ``QLayout`` container
        """
        self.node = node
        print(properties)
        self.properties = properties
        self.settings = settings
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layouts = QVBoxLayout()
        NameLabel = uni_Widget.ICTFELabel()
        NameLabel.setText(self.properties['name'])
        layouts.addWidget(NameLabel)
        for i in self.properties['properties']:
            if self.properties['properties'][i] == bool:
                checks = uni_Widget.ICTFECheckBox()
                layouts.addWidget(checks)
                checks.setText(i)
                self.settingmap[i] = checks
            elif self.properties['properties'][i] == str:
                linetips = uni_Widget.ICTFELabel()
                linetips.setText(i)
                layouts.addWidget(linetips)
                linebox = uni_Widget.ICTFELineBox()
                layouts.addWidget(linebox)
                linebox.setText(self.settings[i])
                layouts.addWidget(linebox)
                self.settingmap[i] = linebox
            elif type(self.properties['properties'][i]) == list:
                comtips = uni_Widget.ICTFELabel()
                comtips.setText(i)
                layouts.addWidget(comtips)
                combobox = QComboBox()
                for j in self.properties['properties'][i]:
                    combobox.addItem(j)
                combobox.setCurrentText(self.settings[i])
                layouts.addWidget(combobox)
                self.settingmap[i] = combobox
            else:
                pass
        self.setLayout(layouts)

    def getSettings(self):
        for i in self.settings:
            if type(self.settingmap[i]) == uni_Widget.ICTFECheckBox:
                self.settings[i] = self.settingmap[i].isChecked()
            elif type(self.settingmap[i]) == uni_Widget.ICTFELineBox:
                self.settings[i] = self.settingmap[i].text()
            elif type(self.settingmap[i]) == QComboBox:
                print(self.settingmap[i].currentText())
                self.settings[i] = self.settingmap[i].currentText()
        return self.settings


class CryptoNode(Node):
    name = 'None'
    op_code = CRYPTO_OP_CODE
    op_title = "Undefined"
    properties = {}
    settings = {}
    outputResult = []
    func = None

    GraphicsNode_class = CryptoGraphicsNode
    NodeContent_class = CryptoContent

    def __init__(self, scene, modules):
        self.properties = modules.properties
        self.settings = modules.defaults
        self.func = modules.main
        outputResult = []
        inputs = []
        for i in range(0, modules.properties['input']):
            inputs.append(2)
        for i in range(0, modules.properties['output']):
            outputResult.append(1)
            self.outputResult.append(None)
        super().__init__(scene, self.__class__.op_title, inputs, outputResult)

        # it's really important to mark all nodes Dirty by default
        self.markDirty()

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def initInnerClasses(self):
        """Sets up graphics Node (PyQt) and Content Widget"""
        node_content_class = self.getNodeContentClass()
        graphics_node_class = self.getGraphicsNodeClass()
        if node_content_class is not None:
            self.content = node_content_class(self, properties=self.properties, settings=self.settings)
        if graphics_node_class is not None:
            self.grNode = graphics_node_class(self)

    def evalOperation(self, inp):
        self.settings = self.content.getSettings()
        print(self.settings)
        return self.func(inp, self.settings)

    def evalImplementation(self):
        inp = []
        for i in range(self.properties['input']):
            inp.append(self.getInput(i))

        for i in inp:
            if i is None:
                self.markInvalid()
                self.markDescendantsDirty()
                self.grNode.setToolTip("请连接所有节点")
                return None
        else:
            inputs = []
            for i in inp:
                outs = i.node.eval()
                if outs is None:
                    return None
                inputs.append(outs[i.count_on_this_node_side - 1])
            val = self.evalOperation(inputs)
            self.outputResult = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def eval(self):
        if not self.isDirty() and not self.isInvalid():
            print(" -> returning cached %s value:" % self.__class__.__name__, self.outputResult)
            return self.outputResult

        try:
            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CryptoNode '%s'" % self.__class__.__name__, "res:", res)
        return res


class CryptoInputContent(QDMNodeContentWidget):
    def initUI(self):
        layouts = QVBoxLayout()
        self.resize(400, 300)
        self.edit = uni_Widget.ICTFETextBox(self)
        self.edit.setPlaceholderText('在这里输入~...')
        self.edit.setObjectName(self.node.content_label_objname)
        layouts.addWidget(self.edit)
        self.setLayout(layouts)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.toPlainText()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.edit.setText(value)
            return True & res
        except Exception as e:
            dumpException(e)
        return res


class CryptoNode_Input(Node):
    op_code = INPUT_OP_CODE
    op_title = "Input"
    content_label_objname = "calc_node_input"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = CryptoInputContent(self)
        self.grNode = CryptoGraphicsNode(self)
        self.content.edit.textChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        self.outputResult = [self.content.edit.toPlainText()]
        self.markDirty(False)
        self.markInvalid(False)
        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("")

        self.evalChildren()

        return self.outputResult

    def eval(self):
        try:
            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()


class CryptoOutputContent(QDMNodeContentWidget):

    def initUI(self):
        self.resize(400,300)
        layouts = QVBoxLayout()
        self.edit = uni_Widget.ICTFETextBox(self)
        self.edit.setPlaceholderText('不出意外的话, 这里应该是输出~...')
        self.edit.setObjectName(self.node.content_label_objname)
        layouts.addWidget(self.edit)
        self.setLayout(layouts)


class CryptoNode_Output(Node):
    icon = "icons/out.png"
    op_code = OUTPUT_OP_CODE
    op_title = "Output"
    content_label_objname = "calc_node_output"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[])

    def initInnerClasses(self):
        self.content = CryptoOutputContent(self)
        self.grNode = CryptoGraphicsNode(self)

    def evalImplementation(self):
        input_node_sockets = self.getInput(0)
        if not input_node_sockets:
            self.grNode.setToolTip("输入未连接")
            self.markInvalid()
            return

        val = input_node_sockets.node.eval()

        if val is None:
            self.grNode.setToolTip("输入不合法")
            self.markInvalid()
            return

        self.content.edit.setText(val[0])
        self.markInvalid(False)
        self.markDirty(False)
        self.grNode.setToolTip("")

        return val

    def eval(self):
        try:
            val = self.evalImplementation()
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()


class CryptoNodeEditorWidget(NodeEditorWidget):
    def __init__(self):
        super().__init__()
        # self.setAttribute(Qt.WA_DeleteOnClose)
        self.scene.addDragEnterListener(self.onDragEnter)
        self.scene.addDropListener(self.onDrop)

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
                    node = CryptoNode_Input(self.scene)
                elif text == 'output':
                    node = CryptoNode_Output(self.scene)
                else:
                    print(Modules[text])
                    node = CryptoNode(self.scene, Modules[text])
                node.setPos(scene_position.x(), scene_position.y())
                self.scene.history.storeHistory("Created node %s" % node.__class__.__name__)
            except Exception as e:
                dumpException(e)

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            # print(" ... drop ignored, not requested format '%s'" % LISTBOX_MIMETYPE)
            event.ignore()
'''
