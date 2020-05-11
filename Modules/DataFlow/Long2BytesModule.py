from Crypto.Util.number import *

properties = {
    'name': 'long to bytes',
    'categories': '字符串操作',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {}
}

defaults = {}


def main(inp, settings):
    return {0: long_to_bytes(int(inp[0]))}
