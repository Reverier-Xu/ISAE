from CryptoPanel.Modules.CaesarModuleUtils import *

properties = {
    'name': 'Caesar',
    'categories': '密码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '模式': ['加密', '解密'],
        '位移': str,
        '数字': bool,
        '步增': str,
        '限制': str
    }
}

defaults = {
    '模式': '加密',
    '位移': '3',
    '数字': False,
    '步增': '0',
    '限制': '26'
}


def main(inp, settings):
    if settings['模式'] == '加密':
        out = {0: CaesarEncrypt(inp[0], int(settings['位移']), settings['数字'], int(settings['步增']), int(settings['限制']))}
        return out
    elif settings['模式'] == '解密':
        out = {0: CaesarDecrypt(inp[0], int(settings['位移']), settings['数字'], int(settings['步增']), int(settings['限制']))}
        return out
    else:
        return None
