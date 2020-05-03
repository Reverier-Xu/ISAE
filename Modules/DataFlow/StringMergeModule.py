__AUTHOR__ = 'Reverier Xu'

properties = {
    'name': '字符串拼接',
    'categories': '字符串操作',
    'input': {0: '前', 1: '后'},
    'output': {0: '输出'},
    'properties': {}
}
defaults = {}


def main(inp, settings):
    print(settings)
    out = {0: inp[0] + inp[1]}
    return out
