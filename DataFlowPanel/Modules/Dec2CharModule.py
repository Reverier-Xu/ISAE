import binascii

properties = {
    'name': 'Dec To Char',
    'categories': '数据转换',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
    }
}
defaults = {
}


def main(inp, settings):
    out = {0: dec2char(inp[0])}
    return out


def dec2char(data: str):
    output = ''
    temp = data.split(' ')
    for i in temp:
        try:
            output += chr(int(i))
        except:
            pass
    return output
