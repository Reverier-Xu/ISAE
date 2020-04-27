from DataFlowPanel.Modules.StrokesModuleUtils import *

properties = {
    'name': '笔画密码',
    'categories': '密码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {}
}

defaults = {}


def main(inp, settings):
    print(settings)
    out = {0: StrokesDecrypt(inp[0])}
    return out
