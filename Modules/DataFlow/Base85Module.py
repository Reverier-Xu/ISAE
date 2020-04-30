import Modules.DataFlow.BaseModuleUtils as Utils

properties = {
    'name': 'Base85-ASCII',
    'categories': '编码解码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '开关': ['编码', '解码'],
        '编码表': str,
        'eval': bool
    }
}

defaults = {
    '开关': '编码',
    '编码表': Utils.Base85StandardTable,
    'eval': False
}


def main(inp: dict, settings: dict):
    out = {}
    if settings['开关'] == '编码':
        out[0] = Utils.ChangeTableBase85Encode(inp[0], settings['编码表'], settings['eval'])
    elif settings['开关'] == '解码':
        out[0] = Utils.ChangeTableBase85Decode(
            inp[0], settings['编码表'])
    return out