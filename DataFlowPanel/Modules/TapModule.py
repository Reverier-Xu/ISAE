properties = {
    'name': 'Tap Code',
    'categories': '编码解码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '开关': ['编码', '解码']
    }
}

defaults = {'开关': '编码'}


def main(inp, settings):
    if settings['开关'] == '编码':
        out = {0: TapEncode(inp[0])}
    else:
        out = {0: TapDecode(inp[0])}
    return out


def TapEncode(text):
    table = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15,
             'F': 21, 'G': 22, 'H': 23, 'I': 24, 'J': 25,
             'L': 31, 'M': 32, 'N': 33, 'O': 34, 'P': 35,
             'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
             'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55,
             'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15,
             'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25,
             'l': 31, 'm': 32, 'n': 33, 'o': 34, 'p': 35,
             'q': 41, 'r': 42, 's': 43, 't': 44, 'u': 45,
             'v': 51, 'w': 52, 'x': 53, 'y': 54, 'z': 55,
             'K': 13, 'k': 13}
    output = ''
    for i in text:
        output += str(table[i]) + ' '
    return output


def TapDecode(text):
    retable = [['A', 'B', '(C/K)', 'D', 'E'],
               ['F', 'G', 'H', 'I', 'J'],
               ['L', 'M', 'N', 'O', 'P'],
               ['Q', 'R', 'S', 'T', 'U'],
               ['V', 'W', 'X', 'Y', 'Z']]
    output = ''
    temp1 = ''
    temp2 = ''
    for i in text:
        if len(temp1) == 1 and len(temp2) == 1:
            output += retable[int(temp1) - 1][int(temp2) - 1]
            temp1 = ''
            temp2 = ''
        if '1' <= i <= '5':
            if len(temp1) == 1:
                temp2 = i
            else:
                temp1 = i
    if len(temp1) == 1 and len(temp2) == 1:
        output += retable[int(temp1)][int(temp2)]
    return output
