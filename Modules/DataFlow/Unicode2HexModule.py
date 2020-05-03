__AUTHOR__ = 'Reverier Xu'

properties = {
    'name': 'Unicode To Hex',
    'categories': '数据转换',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
    }
}
defaults = {}


def main(inp, settings):
    out = {0: Unicode2HexStr(inp[0])}
    return out


def Unicode2HexStr(Unicode_Str):
    hex_str = ""

    for i in range(0, len(Unicode_Str)):
        hex_str += (hex(ord(Unicode_Str[i])).replace('0x', '').zfill(4))

    return hex_str
