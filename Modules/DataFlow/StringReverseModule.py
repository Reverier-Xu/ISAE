__AUTHOR__ = 'Reverier Xu'

properties = {
    'name': '反转',
    'categories': '字符串操作',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '方式': ['按字符', '按行']
    }
}
defaults = {
    '方式': '按字符'
}


def main(inp, settings):
    out = {}
    if settings['方式'] == '按字符':
        out[0] = inp[0][::-1]
    else:
        lines = inp[0].splitlines()
        string = ''
        for i in reversed(lines):
            string += i
            string += '\n'
        out[0] = string
    return out
