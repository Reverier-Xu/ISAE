from .pycipher.polybius import PolybiusSquare

properties = {
    'name': 'Polybius',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
        'switch': ['encrypt', 'decrypt'],
        'key': str,
        'size': str,
        'table': str
    }
}
defaults = {
    'switch': 'encrypt',
    'key': 'phqgiumeaylnofdxkrcvstzwb',
    'size': '5',
    'table': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
}

def main(inp, settings):
    coder = PolybiusSquare(settings['key'], int(settings['size']), settings['table'])
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0])}
    else:
        return {0: coder.decipher(inp[0])}
