from Modules.DataFlow import AvBvUtils as Utils

properties = {
    'name': 'BV -> av',
    'categories': '小工具',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {}
}

defaults = {}


def main(inp, settings):
    return {0: 'av' + str(Utils.dec(inp[0]))}
