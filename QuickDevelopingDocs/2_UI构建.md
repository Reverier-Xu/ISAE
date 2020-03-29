# ICTFE 开发快速上手文档 - 2 UI构建

## 控件绘制

开发ICTFE相关的模块时, 第一步就是绘制相关的控件, 包括大小, 位置, 样式等.

为了保证UI经过不同人开发后的统一性, 同时又能方便UI开发, Reverier基于Qt原始的控件包装了一层样式表.

在相应板块下建立一个文件夹, 命名为`<工具名称>Module`

在这个文件夹下建立`ui_<工具名称>Module.py`

在`ui_<工具名称>Module.py`下的开头导入:

```python
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Widgets import uni_Widget
```

即可快速使用本项目定制的控件.

在`ui_<工具名称>Module.py`中声明一个`ui_<工具名称>Panel`的类, 类继承于`QWidget`, 并定义初始化函数. 就像下面这样:

```python
class ui_xxxPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_xxxPanel, self).__init__() # 调用QWidget的初始化函数
        '''
        在此处绘制控件
        '''
```

接下来进行控件的绘制. ICTFE包装过的统一UI控件有:

* ICTFEButton: 基于QPushButton定制, 就是普通的按钮, 拥有内建的clicked信号.
* ICTFECheckBox: 基于QCheckBox定制的复选框, 拥有检查是否被选中的函数isChecked.
* ICTFELineBox: 基于QLineEdit定制, 允许用于输入单行文本的控件, 可以获取, 设置文本框内的的文本, 并在改变文本时发出文本被改变的信号.
* ICTFETextBox: 基于QTextEdit定制, 屏蔽了原控件的富文本支持, 允许用户输入多行纯文本, 可以获取, 设置文本框内的的文本, 并在改变文本时发出文本被改变的信号.
* ICTFELabel: 基于QLabel定制的Label, 可以在界面上显示一条文本或者图片. Reverier定制了其中的字体与统一外观, 显示图片时等同于QLabel的显示效果.
* ICTFEList: 基于QListBox定制的ListBox, 支持拖动条目, 删除条目, 添加条目.

例如绘制一个按钮:

```python
class ui_xxxPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_xxxPanel, self).__init__() # 调用QWidget的初始化函数

        # Demo Button
        self.DemoButton = uni_Widget.ICTFEButton(self) # 初始化一个按钮, 并把父对象设置为本Pabel.
        self.DemoButton.setObjectName('DemoName') # 用于Qt识别对象的名称. 一般就写对象名.
        self.DemoButton.setGeometry(QtCore.QRect(0, 0, 120, 45))
        # 本句设置按钮的位置和大小, 前两个参数是位置, 表示控件最左上角的像素所处的坐标, 其中x以右为正方向, y以下为正方向, x与y的位置是相对于父控件的最左上角的像素的.
        # 在没有特殊需求的情况下, 尽量把所有的按钮大小都统一为 120 * 45.
        self.DemoButton.setText('Demo') # 在按钮上显示文字 'Demo'
```

每一个控件至少设置前三条属性. 对于Button, Label, CheckBox, 则还需要设置显示的文字, 设置方法统一为`setText()`
