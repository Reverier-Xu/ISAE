from .pycipher.foursquare import Foursquare

properties = {
    'name': '四方密码',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
        'switch': ['encrypt', 'decrypt'],
        'key1': str,
        'key2': str
    }
}
defaults = {
    'switch': 'encrypt',
    'key1': 'zgptfoihmuwdrcnykeqaxvsbl',
    'key2': 'mfnbdcrhsaxyogvituewlqzkp'
}

def main(inp, settings):
    coder = Foursquare(settings['key1'], settings['key2'])
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0])}
    else:
        return {0: coder.decipher(inp[0])}
