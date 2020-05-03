__AUTHOR__ = 'Reverier Xu'

import re

properties = {
    'name': '字符串分割(正则)',
    'categories': '字符串操作',
    'input': {0: '输入'},
    'output': {0: '前', 1: '后'},
    'properties': {
        '表达式': str
    }
}

defaults = {
    '表达式': '[$|#]'
}


def main(inp: dict, settings: dict):
    out = {}
    pattern = settings['表达式']
    outs = re.split(pattern, inp[0], 1)
    out[0] = outs[0]
    try:
        out[1] = outs[1]
    except BaseException:
        out[1] = ''
    return out
