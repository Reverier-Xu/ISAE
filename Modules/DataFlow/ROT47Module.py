from Modules.DataFlow.ROTModuleUtils import *

properties = {
    'name': 'ROT47',
    'categories': '密码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
    }
}
defaults = {
}


def main(inp, settings):
    print(settings)
    out = {0: ROT47(inp[0])}
    return out
