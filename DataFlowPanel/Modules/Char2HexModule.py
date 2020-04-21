import binascii

properties = {
    'name': 'Char To Hex',
    'categories': '数据转换',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {

    }
}
defaults = {

}


def main(inp, settings):
    out = {0: char2hex(inp[0]).decode()}
    return out


def char2hex(data):
    output = binascii.hexlify(data.encode())
    return output
