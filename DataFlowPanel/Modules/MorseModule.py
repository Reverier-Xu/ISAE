import DataFlowPanel.Modules.MorseModuleUtils as utils

properties = {
    'name': 'Morse',
    'categories': '编码解码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '开关': ['编码', '解码'],
        '分隔符': str
    }
}
defaults = {
    '开关': '编码',
    '分隔符': ' '
}


def main(inp, settings):
    if settings['开关'] == '编码':
        out = {0: utils.MorseEncode(inp[0], settings['分隔符'])}
    else:
        out = {0: utils.MorseDecode(inp[0], settings['分隔符'])}
    return out
