from typing import Optional, Any

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_Widgets import uni_Widget
from ui_Widgets.qtpynodeeditor import *
import traceback
from copy import copy
from DataFlowPanel.DataFlowNodeThread import ComputeThread


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
                 PortType.output: 2,
                 }
    port_caption_visible = True
    port_caption = {
        'input': {

        },
        'output': {
            0: 'data',
            1: '路径'
        }
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
            self.file_name, _ = QFileDialog.getOpenFileName(
                None, "打开文件", QtCore.QDir.homePath(),
                "all(*)")
            try:
                with open(self.file_name, 'rb') as out:
                    self._data = out.read()
            except Exception as ex:
                print(f'Failed to load file {self.file_name}: {ex}')
                return False
            self._label.setText(self.file_name)
            self.data_updated.emit(0)
            return True

        return False

    def resizable(self):
        return True

    def out_data(self, port):
        if port == 0:
            return StringData(self._data)
        else:
            return StringData(self.file_name)

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


class FileOutputModel(NodeDataModel):
    name = 'File Output'
    caption = 'File Output'
    caption_visible = True
    port_caption_visible = True
    num_ports = {PortType.input: 1,
                 PortType.output: 0,
                 }
    port_caption = {
        'input': {
            0: '输入'
        },
        'output': {
        }
    }
    data_type = StringData

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._node_data = None
        self._show = uni_Widget.ICTFEButton()
        self._show.setText('无文件...')
        self._show.setEnabled(False)
        self._show.clicked.connect(self.SaveFile)

    def SaveFile(self):
        output_path, file_type = QFileDialog.getSaveFileName(self._show,
                                                             "保存文件",
                                                             '',
                                                             "All Files (*)")
        if output_path == "":
            return
        string = self._node_data.string
        if type(string) == str:
            string = string.encode()
        with open(output_path, 'wb') as out:
            out.write(string)

    def set_in_data(self, node_data, port):
        self._node_data = node_data
        if (self._node_data and
                self._node_data.data_type == StringData.data_type and
                self._node_data.string):
            self._show.setText('点击保存')
            self._show.setEnabled(True)
        else:
            self._show.setText('无文件...')
            self._show.setEnabled(False)

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
        w = 0
        h = 0
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

    def out_data(self, port: int) -> Optional[Any]:
        """
        The output data as a result of this calculation

        Parameters
        ----------
        port : int

        Returns
        -------
        value : NodeData
        """
        try:
            return copy(self.outputs[port])
        except:
            return None

    def set_in_data(self, data: NodeData, port: Port):
        """
        New data at the input of the node

        Parameters
        ----------
        data : NodeData
        port_index : int
        :param data:
        :param port:
        """
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

