from .pycipher.bifid import Bifid

properties = {
    'name': 'Bifid',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
        'switch': ['encrypt', 'decrypt'],
        'key': str,
        'period': str
    }
}
defaults = {
    'switch': 'encrypt',
    'key': 'reverieristhemostactivedeveloper',
    'period': '5'
}

def main(inp, settings):
    coder = Bifid(settings['key'], int(settings['period']))
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0])}
    else:
        return {0: coder.decipher(inp[0])}
