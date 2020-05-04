from .pycipher.playfair import Playfair

properties = {
    'name': 'Play Fair',
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
    'key': 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
}

def main(inp, settings):
    coder = Playfair(settings['key'])
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0])}
    else:
        return {0: coder.decipher(inp[0])}
