properties = {
    'name': 'Char To Binary',
    'categories': '数据转换',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {}
}
defaults = {}


def main(inp, settings):
    out = {0: encode(inp[0])}
    return out


def encode(s):
    return ''.join([bin(ord(c)).replace('0b', '') for c in s])


def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
