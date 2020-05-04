from .pycipher.atbash import Atbash

properties = {
    'name': 'Atbash',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
        'switch': ['encrypt', 'decrypt'],
        '保留标点': bool
    }
}
defaults = {
    'switch': 'encrypt',
    '保留标点': False
}

def main(inp, settings):
    coder = Atbash()
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0], settings['保留标点'])}
    else:
        return {0: coder.decipher(inp[0], settings['保留标点'])}
