__AUTHOR__ = 'Reverier Xu'

import binascii

properties = {
    'name': 'Hex To Char',
    'categories': '数据转换',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {

    }
}
defaults = {

}


def main(inp, settings):
    print(settings)
    out = {}
    try:
        out[0] = hex2char(inp[0]).decode()
    except:
        out[0] = str(hex2char(inp[0]))
    return out


def hex2char(data):
    output = binascii.unhexlify(data.encode())
    return output
