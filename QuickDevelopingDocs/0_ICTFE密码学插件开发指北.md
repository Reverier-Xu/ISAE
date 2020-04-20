# ICTFE 开发快速上手文档 - 0 密码学插件开发快速指北

## 介绍

ICTFE的密码学部分采用了动态节点编辑器的方式构建而成, 参与相关功能开发的开发者无需再次考虑GUI布局等问题,
只需要依据特定的格式编写相关函数即可.

## 一般格式

想将某个功能添加到ICTFE内, 你需要在`CryptoPanel/Modules`下面建立一个文件, 为后期管理方便,
请将功能主文件命名为: `xxxModule.py`, 其他的辅助类文件命名为`xxxModuleUtils.py`.

你可以不遵守此类文件的命名规则, 也一样可以使用, 但是可能会给后期的管理带来一定的麻烦.

## 主文件格式

主文件应当包含:

### 插件属性

例如Base64模块的属性为:

```python
properties = {
    'name': 'Base64',
    'categories': '编码解码',
    'input': {0:'输入'},
    'output': {0:'输出'},
    'properties': {
        '开关': ['编码', '解码'],
        '编码表': str,
        'eval': bool
    }
}
```

每个模块的属性名称都应该为`properties`. 如果另取名称, 插件将不会正常工作.

`properties`为`Python`格式的字典, 其中必须包括:

* `'name'`: 模块的名称;
* `'categories`: 模块所属分区, 你可以将插件加入一个当前现有的分区, 也可以新建一个分区, 只需要填写不同的名称即可.
* `'input'`: 模块的输入端口. 这个端口应该为一个字典, 其中应包括从0开始编号的各个端口的名称. 端口数量随意.
* `'output'`: 模块的输出端口, 同上.
* `'properties'`: 模块要进行设置的属性, 如果没有请将其声明为空字典, 切勿不填.

关于`'properties'`项的结构, 有以下三种:

* `'名称': bool`: 代表bool类型的配置项. ICTFE将会以复选框的形式绘制此项. 此项一般为某个开关变量, 比如是否对输入使用`eval`, 输入是否是大文件等.
* `'名称': str`: 代表用户可填写的配置项. ICTFE将会以单行文本框的形式绘制此项. 此项一般是可以自定义的编码表等变量, 比如换表Base64的`table`等.
* `'名称': ['选项1', '选项2', ...]`: 代表用户可选择的菜单. ICTFE将会以下拉式菜单绘制此项. 此项一般是供用户进行单项选择的配置项, 例如编码还是解码等.

仅支持此三种配置方式, 其他方式不会奏效, 并可能引发软件崩溃.

除了`properties`项之外, 你应当还添加默认配置, 例如Base64模块:

```python
defaults = {
    '开关': '编码',
    '编码表': 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',
    'eval': False
}
```

请注意默认配置`defaults`中的各个项应当和`properties['properties']`中写明的类型保持完全一致. 否则可能导致软件崩溃.

最后是主调函数`main`.

main函数的一般格式如下:

```python
def main(inp: dict, settings: dict):
    out = {}
    ''' 你的处理 '''
    return out
```

`main`必须包含两个参数, 第一个参数是输入, 以字典的形式组织, 格式为`{端口号(int): 数据(str)}`. 第二个参数为设置项, 其格式与`defaults`保持一致. 请根据设置项和输入来计算输出. 输出同样也是一个字典, 格式为`{端口号(int): 输出数据(str)}`.

例如Base64模块的`main`函数:

```python
def main(inp: dict, settings: dict):
    out = {}
    if settings['开关'] == '编码':
        out[0] = utils.ChangeTableBase64Encode(inp[0], settings['编码表'], settings['eval'])
    elif settings['开关'] == '解码':
        out[0] = utils.ChangeTableBase64Decode(
            inp[0], settings['编码表'])
    return out
```

`defaults`, `properties`, `main`为一个模块中必须包含的三个项. 除此之外, 你可以在模块中任意定义其他函数或者变量, 导入任意模块使用.

不包含`properties`项的py文件将不会导入到ICTFE中. 所以你可以在`xxxModuleUtils.py`中任意编写, ICTFE扫描目录时将会忽略此模块.

接下来打开ICTFE, 一切都将照常工作. 如果输入不合法, 模块会自动停止计算, 因此不用担心异常处理.

需要注意的是, 你所便携的模块在导入和绘制的阶段可能导致整个ICTFE的崩溃, 因此你应该对你所编写的模块负责. 如果你的模块导致崩溃, 请不要将其推送到仓库.
