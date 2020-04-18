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
