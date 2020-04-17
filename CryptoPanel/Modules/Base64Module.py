import CryptoPanel.Modules.BaseModuleUtils as utils
properties = {
    'name': 'Base64',
    'categlories': 'Encode/Decode',
    'input': 1,
    'output': 1,
    'properties': {
        '开关': ['编码', '解码'],
        '编码表': str,
        'eval': bool
    }
}

default = {
    'input': {0: ''},
    'output': {0: ''},
    'properties': {
        '开关': '编码',
        '编码表': 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',
        'eval': False
    }
}

def main(dic: dict):
    if dic['properties']['开关'] == '编码':
        dic['output'][0] = utils.ChangeTableBase64Encode(dic['input'][0], dic['properties']['编码表'], dic['properties']['eval'])
    elif dic['properties']['开关'] == '解码':
        dic['output'][0] = utils.ChangeTableBase64Decode(
            dic['input'][0], dic['properties']['编码表'], dic['properties']['eval'])
    return dic
