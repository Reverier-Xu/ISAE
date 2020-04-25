import copy

from PyQt5 import QtCore, QtWidgets, Qt, QtGui
from DataFlowPanel.ui_DataFlowPanel import ui_CryptoPanel
from ui_Widgets import uni_Widget
from DataFlowPanel.DataFlowNodeBasic import *
from ui_Widgets.qtpynodeeditor import *


class DataFlowPanel(ui_CryptoPanel):
    def __init__(self):
        super(DataFlowPanel, self).__init__()
        self.ToolsSearchBox.textChanged.connect(self.ToolsList.filter)
        self.ToolsList.addDIYItem('Input', '基本')
        self.ToolsList.addDIYItem('File Input', '基本')
        self.ToolsList.addDIYItem('Output', '基本')
        self.ToolsList.addDIYItem('Image Output', '基本')
        self.ToolsList.addDIYItem('File Output', '基本')
        for i in Modules:
            self.ToolsList.addDIYItem(i, Modules[i].properties['categories'])
        reg = DataModelRegistry()
        reg.register_model(InputModel, category='Basic')
        reg.register_model(OutputModel, category='Basic')
        reg.register_model(ImageShowModel, category='Basic')
        reg.register_model(FileInputModel, category='Basic')
        reg.register_model(FileOutputModel, category='Basic')
        for i in Modules:
            class DIYNodesDataModule(CryptoComputeModel):
                port_caption_visible = True
                data_type = StringData.data_type
                module = Modules[i]
                properties = module.properties
                num_ports = {PortType.input: len(module.properties['input']),
                             PortType.output: len(module.properties['output'])}
                port_caption = {'input': module.properties['input'],
                                'output': module.properties['output']}
                name = Modules[i].properties['name']

                def __init__(self, *args, **kwargs):
                    self.settings = copy(self.module.defaults)
                    self.func = self.module.main
                    self.inputs = {}
                    self.outputs = {}
                    super().__init__(self.module, *args, **kwargs)

            reg.register_model(DIYNodesDataModule, category=Modules[i].properties['categories'])
        scene = FlowScene(reg)
        self.CryptoToolNodeEditor.setScene(scene)
        self.CryptoToolNodeEditor.scene.node_double_clicked.connect(self.OptionsBox.LoadOptions)
        self.SaveOptionsButton.clicked.connect(self.SaveOptionsFunc)

    def SaveOptionsFunc(self):
        try:
            self.OptionsBox.node.model.settings = self.OptionsBox.GetOptions()
        except:
            pass
