from .pycipher.autokey import Autokey

properties = {
    'name': '自动密钥机',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
        'switch': ['encrypt', 'decrypt'],
        'key': str
    }
}
defaults = {
    'switch': 'encrypt',
    'key': 'REVERIERTQL'
}

def main(inp, settings):
    coder = Autokey(settings['key'])
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0])}
    else:
        return {0: coder.decipher(inp[0])}
