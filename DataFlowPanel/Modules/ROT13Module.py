from DataFlowPanel.Modules.ROTModuleUtils import *

properties = {
    'name': 'ROT13',
    'categories': '密码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
    }
}
defaults = {
}


def main(inp, settings):
    out = {0: ROT13(inp[0])}
    return out
