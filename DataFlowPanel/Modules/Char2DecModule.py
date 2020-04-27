properties = {
    'name': 'Char To Dec',
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
    out = {0: char2dec(inp[0])}
    return out


def char2dec(data):
    output = ''
    for i in data:
        output += str(ord(i)) + ' '
    return output
