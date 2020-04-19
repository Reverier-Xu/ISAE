import CryptoPanel.Modules.BaseModuleUtils as utils
properties = {
    'name': 'Base64',
    'categlories': '编码解码',
    'input': {0:'输入'},
    'output': {0:'输出'},
    'properties': {
        '开关': ['编码', '解码'],
        '编码表': str,
        'eval': bool
    }
}

defaults = {
    '开关': '编码',
    '编码表': 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',
    'eval': False
}


def main(inp: dict, settings: dict):
    out = []
    if settings['开关'] == '编码':
        out.append(utils.ChangeTableBase64Encode(inp[0], settings['编码表'], settings['eval']))
    elif settings['开关'] == '解码':
        out.append(utils.ChangeTableBase64Decode(
            settings[0], settings['编码表']))
    return out
