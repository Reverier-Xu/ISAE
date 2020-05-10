from Modules.DataFlow import AvBvUtils as Utils

properties = {
    'name': 'av -> BV',
    'categories': '小工具',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {}
}

defaults = {}


def main(inp, settings):
    return {0: Utils.enc(int(inp[0][2:]))}
