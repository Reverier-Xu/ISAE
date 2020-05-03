__AUTHOR__ = 'Reverier Xu'

import traceback

properties = {
    'name': 'Hex To Bytes',
    'categories': '数据转换',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
    }
}

defaults = {}


def main(inp, settings):
    try:
        return {0: bytes.fromhex(inp[0])}
    except:
        traceback.print_exc()
