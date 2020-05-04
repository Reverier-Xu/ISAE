from .pycipher.adfgvx import ADFGVX

properties = {
    'name': 'ADFGVX',
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
    'key': 'ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8',
    'keyword': 'REVERIER'
}

def main(inp, settings):
    coder = ADFGVX(settings['key'], settings['keyword'])
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0])}
    else:
        return {0: coder.decipher(inp[0])}