from .pycipher.simplesubstitution import SimpleSubstitution

properties = {
    'name': '简单换位密码',
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
    'key': 'AJPCZWRLFBDKOTYUQGENHXMIVS'
}

def main(inp, settings):
    coder = SimpleSubstitution(settings['key'])
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0])}
    else:
        return {0: coder.decipher(inp[0])}
