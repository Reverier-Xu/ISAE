from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui_Widgets.nodeeditor.node_node import Node
from ui_Widgets.nodeeditor.node_content_widget import QDMNodeContentWidget
from ui_Widgets.nodeeditor.node_graphics_node import QDMGraphicsNode
from ui_Widgets.nodeeditor.node_socket import LEFT_CENTER, RIGHT_CENTER
from ui_Widgets.nodeeditor.utils import dumpException
from ui_Widgets import uni_Widget
from PyQt5 import QtCore


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


PropertiesSample = {
    'name': 'test',
    'input': 2,
    'output': 1,
    'properties': {
        'testins': str,
        'testcheck': bool,
        'testchoose': ['a', 'b', 'c']
    }
}


class CryptoNodeContent(QDMNodeContentWidget):
    def initUI(self):
        self.layouts = QVBoxLayout(self)
        lbl = uni_Widget.ICTFELabel(self.node.content_label)
        lbl.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        lbl.setObjectName(self.node.content_label_objname)
        self.layouts.addWidget(lbl)


class CryptoNode(Node):
    icon = ""
    op_code = 0
    op_title = "CryptoNode"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = CryptoGraphicsNode
    NodeContent_class = CryptoNodeContent

    def __init__(self, scene, properties: dict = None):
        self.prop = properties
        inputs = []
        outputs = []
        self.content_label = properties['name']
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
