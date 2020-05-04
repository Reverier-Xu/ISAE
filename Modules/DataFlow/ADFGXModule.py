from .pycipher.adfgx import ADFGX

properties = {
    'name': 'ADFGX',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
        'switch': ['encrypt', 'decrypt'],
        'key': str,
        'keyword': str
    }
}

defaults = {
    'switch': 'encrypt',
    'key': 'phqgmeaylnofdxkrcvszwbuti',
    'keyword': 'REVERIER'
}

def main(inp, settings):
    coder = ADFGX(settings['key'], settings['keyword'])
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0])}
    else:
        return {0: coder.decipher(inp[0])}