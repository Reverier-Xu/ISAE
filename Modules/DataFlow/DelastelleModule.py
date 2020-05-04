from .pycipher.delastelle import Delastelle

properties = {
    'name': 'Delastelle',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
        'switch': ['encrypt', 'decrypt'],
        'key': str,
        'table': str
    }
}
defaults = {
    'switch': 'encrypt',
    'key': 'phqgiumeaylnofdxkrcvst.zwb',
    'table': '123'
}

def main(inp, settings):
    coder = Delastelle(settings['key'], settings['table'])
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0])}
    else:
        return {0: coder.decipher(inp[0])}
