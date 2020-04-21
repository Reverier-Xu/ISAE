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


def Unicode2HexStr(Unicde_Str):
    Hex_Str = ""

    for i in range(0, len(Unicde_Str)):
        Hex_Str += (hex(ord(Unicde_Str[i])).replace('0x', '').zfill(4))

    return Hex_Str
