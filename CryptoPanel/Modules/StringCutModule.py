properties = {
    'name': '字符串分割',
    'categories': '字符串操作',
    'input': {0: '输入'},
    'output': {0: '前', 1: '后'},
    'properties': {
        '位置': str
    }
}

defaults = {
    '位置': '2'
}


def main(inp: dict, settings: dict):
    out = {0: inp[0][0:int(settings['位置'])], 1: inp[0][int(settings['位置']):]}
    return out
