__AUTHOR__ = 'Reverier Xu'

properties = {
    'name': '字符去除/替换',
    'categories': '字符串操作',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '去除': str,
        '替换': str
    }
}

defaults = {
    '去除': '',
    '替换': ''
}


def main(inp, settings):
    out = {0: inp[0].replace(settings['去除'], settings['替换'])}
    return out
