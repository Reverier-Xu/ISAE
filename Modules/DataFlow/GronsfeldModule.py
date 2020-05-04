from .pycipher.gronsfeld import Gronsfeld

properties = {
    'name': 'Gronsfeld',
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
    'key': '0123456789'
}

def main(inp, settings):
    keys = settings['key']
    keys = keys.split()
    inps = []
    for i in keys:
        inps.append(int(i))
    coder = Gronsfeld(inps)
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0])}
    else:
        return {0: coder.decipher(inp[0])}
