properties = {
    'name': 'xor',
    'categories': '字符串操作',
    'input': {0: 'origin', 1: 'pattern'},
    'output': {0: 'output'},
    'properties': {}
}

defaults = {}


def main(inp, settings):
    origin = repr(inp[0])
    pattern = repr(inp[1])
    i = 0
    j = 0
    out = ''
    while i < len(origin):
        out += chr(ord(origin[i]) ^ ord(pattern[j]))
        i += 1
        j += 1
        j %= len(pattern)
    return {0: out}
