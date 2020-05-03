__AUTHOR__ = 'Reverier Xu'

import copy

from DataFlowPanel.DataFlowNodeEditor import *
from DataFlowPanel.ui_DataFlowPanel import ui_DataFlowPanel
from ui_Widgets.qtpynodeeditor import *

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


def ScanModules():
    Modules.clear()
    for module in get_modules('Modules/DataFlow'):
        module = importlib.import_module(module, 'Modules.DataFlow')
        try:
            Modules[module.properties['name']] = module
        except:
            pass


class DataFlowPanel(ui_DataFlowPanel):
    def __init__(self):
        super(DataFlowPanel, self).__init__()
        self.ToolsSearchBox.textChanged.connect(self.ToolsList.filter)
        self.RegisterModule()
        try:
            self.CryptoToolNodeEditor.scene.load('UserConfig/NodeEditorCurrent.rxf')
        except:
            pass
        self.SaveButton.clicked.connect(lambda **kwargs: self.CryptoToolNodeEditor._scene.save())

    def RegisterModule(self):
        self.ToolsList.clear()
        ScanModules()
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

                def save(self):
                    doc = super().save()
                    if self.settings:
                        doc['settings'] = self.settings
                    return doc

                def restore(self, doc: dict):
                    try:
                        value = copy(doc["settings"])
                    except Exception:
                        ...
                    else:
                        self.settings = value

            reg.register_model(DIYNodesDataModule,
                               category=Modules[i].properties['categories'])
        scene = FlowScene(reg)
        self.CryptoToolNodeEditor.setScene(scene)
        self.CryptoToolNodeEditor.scene.node_double_clicked.connect(
            self.OptionsBox.LoadOptions)

    def closeEvent(self, QCloseEvent):
        self.CryptoToolNodeEditor.scene.save('UserConfig/NodeEditorCurrent.rxf')
