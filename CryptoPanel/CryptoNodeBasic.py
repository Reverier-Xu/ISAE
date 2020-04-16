import contextlib
import threading

from PyQt5.QtWidgets import QWidget

import ui_Widgets.qtpynodeeditor as ne
from ui_Widgets.qtpynodeeditor import NodeValidationState, NodeData, Port
from ui_Widgets import uni_Widget


class StringData(ne.NodeData):
    data_type = ne.NodeDataType('string', 'string')

    def __init__(self, string: str = ''):
        self._string = string
        self._lock = threading.RLock()

    @property
    def lock(self):
        return self._lock

    @property
    def text(self) -> str:
        """The number data"""
        return self._string


class OutputModel(ne.NodeDataModel):
    name = "Output"
    node_style = None
    data_type = StringData.data_type
    caption_visible = False
    num_ports = {ne.PortType.input: 1,
                 ne.PortType.output: 0,
                 }
    port_caption = {'input': {0: 'output'}}

    def __init__(self, style=None, parent=None):
        super().__init__(style=style, parent=parent)
        self._string = None
        self._label = uni_Widget.ICTFETextBox()
        self._validation_state = NodeValidationState.warning
        self._validation_message = 'Uninitialized'

    def set_in_data(self, data: StringData, port: Port):
        """
        New data propagated to the input

        Parameters
        ----------
        data : NodeData
        port : Port
        """
        self._string = data
        number_ok = (self._string is not None and
                     self._string.data_type.id == 'string')

        if number_ok:
            self._validation_state = NodeValidationState.valid
            self._validation_message = ''
            self._label.setText(self._string.text)
        else:
            self._validation_state = NodeValidationState.warning
            self._validation_message = 'Missing or incorrect inputs'
            self._label.clear()

        self._label.adjustSize()

    def embedded_widget(self) -> QWidget:
        """The number display has a label"""
        return self._label


class InputModel(ne.NodeDataModel):
    name = "Input"
    node_style = None
    caption_visible = False
    num_ports = {ne.PortType.input: 0,
                 ne.PortType.output: 1,
                 }
    port_caption = {'output': {0: 'Result'}}
    data_type = StringData.data_type

    def __init__(self, style=None, parent=None):
        super().__init__(style=style, parent=parent)
        self._string = None
        self._line_edit = uni_Widget.ICTFETextBox()
        self._line_edit.setMaximumSize(self._line_edit.sizeHint())
        self._line_edit.textChanged.connect(self.on_text_edited)
        self._line_edit.setPlaceholderText('输入...')

    @property
    def text(self):
        return self._text

    def save(self) -> dict:
        """Add to the JSON dictionary to save the state of the Input"""
        doc = super().save()
        if self._string:
            doc['text'] = self._text.text
        return doc

    def restore(self, state: dict):
        """Restore the number from the JSON dictionary"""
        try:
            value = state['text']
        except Exception:
            ...
        else:
            self._string = StringData(value)
            self._line_edit.setText(self._text.text)

    def out_data(self, port: int) -> NodeData:
        """
        The data output from this node

        Parameters
        ----------
        port : int

        Returns
        -------
        value : NodeData
        """
        return self._text

    def embedded_widget(self) -> QWidget:
        """The number source has a line edit widget for the user to type in"""
        return self._line_edit

    def on_text_edited(self, string: str):
        """
        Line edit text has changed

        Parameters
        ----------
        string : str
        """
        try:
            text = self._line_edit.toPlainText()
        except ValueError:
            self._data_invalidated.emit(0)
        else:
            self._text = StringData(text)
            self.data_updated.emit(0)


class CryptoNode11(ne.NodeDataModel):
    properties = {}
    caption_visible = True
    num_ports = {
        'input': 1,
        'output': 1,
    }
    port_caption_visible = True
    data_type = StringData.data_type

    def __init__(self, style=None, parent=None):
        super().__init__(style=style, parent=parent)
        self._string1 = None
        self._result1 = None
        self._validation_state = NodeValidationState.warning
        self._validation_message = '未定义的'

    @property
    def caption(self):
        return self.name

    def _check_inputs(self):
        number1_ok = (self._string1 is not None and
                      self._string1.data_type.id == 'string')

        if not number1_ok:
            self._validation_state = NodeValidationState.warning
            self._validation_message = "Missing or incorrect inputs"
            self._result1 = None
            self.data_updated.emit(0)
            return False

        self._validation_state = NodeValidationState.valid
        self._validation_message = ''
        return True

    @contextlib.contextmanager
    def _compute_lock(self):
        if not self._string1:
            raise RuntimeError('inputs unset')

        with self._string1.lock:
            yield

        self.data_updated.emit(0)

    def out_data(self, port: int) -> NodeData:
        """
        The output data as a result of this calculation

        Parameters
        ----------
        port : int

        Returns
        -------
        value : NodeData
        """
        return self._result1

    def set_in_data(self, data: NodeData, port: Port):
        """
        New data at the input of the node

        Parameters
        ----------
        data : NodeData
        port : Port
        """
        if port.index == 0:
            self._string1 = data

        if self._check_inputs():
            with self._compute_lock():
                self.compute(self.properties)

    def validation_state(self) -> NodeValidationState:
        return self._validation_state

    def validation_message(self) -> str:
        return self._validation_message

    def compute(self, prop=None):
        ...


class CryptoNode21(ne.NodeDataModel):
    properties = {}
    caption_visible = True
    num_ports = {
        'input': 2,
        'output': 1,
    }
    port_caption_visible = True
    data_type = StringData.data_type

    def __init__(self, style=None, parent=None):
        super().__init__(style=style, parent=parent)
        self._string1 = None
        self._string2 = None
        self._result1 = None
        self._validation_state = NodeValidationState.warning
        self._validation_message = '未定义的'

    @property
    def caption(self):
        return self.name

    def _check_inputs(self):
        number1_ok = (self._string1 is not None and
                      self._string1.data_type.id == 'string')
        number2_ok = (self._string2 is not None and
                      self._string2.data_type.id == 'string')

        if not number1_ok or not number2_ok:
            self._validation_state = NodeValidationState.warning
            self._validation_message = "Missing or incorrect inputs"
            self._result1 = None
            self.data_updated.emit(0)
            return False

        self._validation_state = NodeValidationState.valid
        self._validation_message = ''
        return True

    @contextlib.contextmanager
    def _compute_lock(self):
        if not self._string1 or not self._string2:
            raise RuntimeError('inputs unset')

        with self._string1.lock:
            with self._string2.lock:
                yield

        self.data_updated.emit(0)

    def out_data(self, port: int) -> NodeData:
        """
        The output data as a result of this calculation

        Parameters
        ----------
        port : int

        Returns
        -------
        value : NodeData
        """
        return self._result1

    def set_in_data(self, data: NodeData, port: Port):
        """
        New data at the input of the node

        Parameters
        ----------
        data : NodeData
        port : Port
        """
        if port.index == 0:
            self._string1 = data
        if port.index == 1:
            self._string2 = data

        if self._check_inputs():
            with self._compute_lock():
                self.compute(self.properties)

    def validation_state(self) -> NodeValidationState:
        return self._validation_state

    def validation_message(self) -> str:
        return self._validation_message

    def compute(self, prop=None):
        ...


class CryptoNode22(ne.NodeDataModel):
    properties = {}
    caption_visible = True
    num_ports = {
        'input': 2,
        'output': 1,
    }
    port_caption_visible = True
    data_type = StringData.data_type

    def __init__(self, style=None, parent=None):
        super().__init__(style=style, parent=parent)
        self._string1 = None
        self._string2 = None
        self._result1 = None
        self._result2 = None
        self._validation_state = NodeValidationState.warning
        self._validation_message = '未定义的'

    @property
    def caption(self):
        return self.name

    def _check_inputs(self):
        number1_ok = (self._string1 is not None and
                      self._string1.data_type.id == 'string')
        number2_ok = (self._string2 is not None and
                      self._string2.data_type.id == 'string')

        if not number1_ok or not number2_ok:
            self._validation_state = NodeValidationState.warning
            self._validation_message = "Missing or incorrect inputs"
            self._result1 = None
            self._result2 = None
            self.data_updated.emit(0)
            return False

        self._validation_state = NodeValidationState.valid
        self._validation_message = ''
        return True

    @contextlib.contextmanager
    def _compute_lock(self):
        if not self._string1:
            raise RuntimeError('inputs unset')

        with self._string1.lock:
            with self._string2.lock:
                yield

        self.data_updated.emit(0)

    def out_data(self, port: int) -> NodeData:
        """
        The output data as a result of this calculation

        Parameters
        ----------
        port : int

        Returns
        -------
        value : NodeData
        """
        if port == 0:
            return self._result1
        if port == 1:
            return self._result2

    def set_in_data(self, data: NodeData, port: Port):
        """
        New data at the input of the node

        Parameters
        ----------
        data : NodeData
        port : Port
        """
        if port.index == 0:
            self._string1 = data
        if port.index == 1:
            self._string2 = data

        if self._check_inputs():
            with self._compute_lock():
                self.compute(self.properties)

    def validation_state(self) -> NodeValidationState:
        return self._validation_state

    def validation_message(self) -> str:
        return self._validation_message

    def compute(self, prop=None):
        ...


class CryptoNode31(ne.NodeDataModel):
    properties = {}
    caption_visible = True
    num_ports = {
        'input': 3,
        'output': 1,
    }
    port_caption_visible = True
    data_type = StringData.data_type

    def __init__(self, style=None, parent=None):
        super().__init__(style=style, parent=parent)
        self._string1 = None
        self._string2 = None
        self._string3 = None
        self._result1 = None
        self._validation_state = NodeValidationState.warning
        self._validation_message = '未定义的'

    @property
    def caption(self):
        return self.name

    def _check_inputs(self):
        number1_ok = (self._string1 is not None and
                      self._string1.data_type.id == 'string')
        number2_ok = (self._string2 is not None and
                      self._string2.data_type.id == 'string')
        number3_ok = (self._string3 is not None and
                      self._string3.data_type.id == 'string')

        if not number1_ok or not number2_ok or not number3_ok:
            self._validation_state = NodeValidationState.warning
            self._validation_message = "Missing or incorrect inputs"
            self._result1 = None
            self.data_updated.emit(0)
            return False

        self._validation_state = NodeValidationState.valid
        self._validation_message = ''
        return True

    @contextlib.contextmanager
    def _compute_lock(self):
        if not self._string1 or not self._string2 or not self._string3:
            raise RuntimeError('inputs unset')

        with self._string1.lock:
            with self._string2.lock:
                with self._string3.lock:
                    yield

        self.data_updated.emit(0)

    def out_data(self, port: int) -> NodeData:
        """
        The output data as a result of this calculation

        Parameters
        ----------
        port : int

        Returns
        -------
        value : NodeData
        """
        return self._result1

    def set_in_data(self, data: NodeData, port: Port):
        """
        New data at the input of the node

        Parameters
        ----------
        data : NodeData
        port : Port
        """
        if port.index == 0:
            self._string1 = data
        if port.index == 1:
            self._string2 = data
        if port.index == 2:
            self._string3 = data

        if self._check_inputs():
            with self._compute_lock():
                self.compute(self.properties)

    def validation_state(self) -> NodeValidationState:
        return self._validation_state

    def validation_message(self) -> str:
        return self._validation_message

    def compute(self, prop=None):
        ...


class CryptoNode32(ne.NodeDataModel):
    properties = {}
    caption_visible = True
    num_ports = {
        'input': 3,
        'output': 2,
    }
    port_caption_visible = True
    data_type = StringData.data_type

    def __init__(self, style=None, parent=None):
        super().__init__(style=style, parent=parent)
        self._string1 = None
        self._string2 = None
        self._string3 = None
        self._result1 = None
        self._result2 = None
        self._validation_state = NodeValidationState.warning
        self._validation_message = '未定义的'

    @property
    def caption(self):
        return self.name

    def _check_inputs(self):
        number1_ok = (self._string1 is not None and
                      self._string1.data_type.id == 'string')
        number2_ok = (self._string2 is not None and
                      self._string2.data_type.id == 'string')
        number3_ok = (self._string3 is not None and
                      self._string3.data_type.id == 'string')

        if not number1_ok or not number2_ok or not number3_ok:
            self._validation_state = NodeValidationState.warning
            self._validation_message = "Missing or incorrect inputs"
            self._result1 = None
            self.data_updated.emit(0)
            return False

        self._validation_state = NodeValidationState.valid
        self._validation_message = ''
        return True

    @contextlib.contextmanager
    def _compute_lock(self):
        if not self._string1 or not self._string2 or not self._string3:
            raise RuntimeError('inputs unset')

        with self._string1.lock:
            with self._string2.lock:
                with self._string3.lock:
                    yield

        self.data_updated.emit(0)

    def out_data(self, port: int) -> NodeData:
        """
        The output data as a result of this calculation

        Parameters
        ----------
        port : int

        Returns
        -------
        value : NodeData
        """
        if port == 0:
            return self._result1
        elif port == 1:
            return self._result2

    def set_in_data(self, data: NodeData, port: Port):
        """
        New data at the input of the node

        Parameters
        ----------
        data : NodeData
        port : Port
        """
        if port.index == 0:
            self._string1 = data
        if port.index == 1:
            self._string2 = data
        if port.index == 2:
            self._string3 = data

        if self._check_inputs():
            with self._compute_lock():
                self.compute(self.properties)

    def validation_state(self) -> NodeValidationState:
        return self._validation_state

    def validation_message(self) -> str:
        return self._validation_message

    def compute(self, prop=None):
        ...


class CryptoNode33(ne.NodeDataModel):
    properties = {}
    caption_visible = True
    num_ports = {
        'input': 3,
        'output': 3,
    }
    port_caption_visible = True
    data_type = StringData.data_type

    def __init__(self, style=None, parent=None):
        super().__init__(style=style, parent=parent)
        self._string1 = None
        self._string2 = None
        self._string3 = None
        self._result1 = None
        self._result2 = None
        self._result3 = None
        self._validation_state = NodeValidationState.warning
        self._validation_message = '未定义的'

    @property
    def caption(self):
        return self.name

    def _check_inputs(self):
        number1_ok = (self._string1 is not None and
                      self._string1.data_type.id == 'string')
        number2_ok = (self._string2 is not None and
                      self._string2.data_type.id == 'string')
        number3_ok = (self._string3 is not None and
                      self._string3.data_type.id == 'string')

        if not number1_ok or not number2_ok or not number3_ok:
            self._validation_state = NodeValidationState.warning
            self._validation_message = "Missing or incorrect inputs"
            self._result1 = None
            self.data_updated.emit(0)
            return False

        self._validation_state = NodeValidationState.valid
        self._validation_message = ''
        return True

    @contextlib.contextmanager
    def _compute_lock(self):
        if not self._string1 or not self._string2 or not self._string3:
            raise RuntimeError('inputs unset')

        with self._string1.lock:
            with self._string2.lock:
                with self._string3.lock:
                    yield

        self.data_updated.emit(0)

    def out_data(self, port: int) -> NodeData:
        """
        The output data as a result of this calculation

        Parameters
        ----------
        port : int

        Returns
        -------
        value : NodeData
        """
        if port == 0:
            return self._result1
        elif port == 1:
            return self._result2
        elif port == 2:
            return self._result3

    def set_in_data(self, data: NodeData, port: Port):
        """
        New data at the input of the node

        Parameters
        ----------
        data : NodeData
        port : Port
        """
        if port.index == 0:
            self._string1 = data
        if port.index == 1:
            self._string2 = data
        if port.index == 2:
            self._string3 = data

        if self._check_inputs():
            with self._compute_lock():
                self.compute(self.properties)

    def validation_state(self) -> NodeValidationState:
        return self._validation_state

    def validation_message(self) -> str:
        return self._validation_message

    def compute(self, prop=None):
        ...
