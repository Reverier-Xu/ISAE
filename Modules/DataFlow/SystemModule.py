import os

properties = {
    'name': 'System',
    'categories': '系统工具',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {}
}

defaults = {}


def main(inp, settings):
    with os.popen(inp[0], 'r') as f:
        s = f.read()
    return {0: s}
