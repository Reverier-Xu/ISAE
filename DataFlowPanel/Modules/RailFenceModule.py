from DataFlowPanel.Modules.RailFenceModuleUtils import *

properties = {
    'name': '栅栏密码',
    'categories': '密码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '开关': ['加密', '解密'],
        '位移': str
    }
}
defaults = {
    '开关': '加密',
    '位移': '3'
}


def main(inp, settings):
    if settings['开关'] == '加密':
        out = {0: RailFenceEncrypt(inp[0], int(settings['位移']))}
    else:
        out = {0: RailFenceDecrypt(inp[0], int(settings['位移']))}
    return out
