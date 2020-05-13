properties = {
    'name': 'Repeat',
    'categories': '字符串操作',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
        'times': str
    }
}

defaults = {
    'times': '10'
}


def main(inp, settings):
    return {0: inp[0] * int(settings['times'])}
