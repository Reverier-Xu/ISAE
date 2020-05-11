from Crypto.Util.number import *

properties = {
    'name': 'bytes to long',
    'categories': '字符串操作',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {}
}

defaults = {}


def main(inp, settings):
    return {0: bytes_to_long((inp[0]))}
