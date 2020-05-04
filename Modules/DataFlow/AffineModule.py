from .pycipher.affine import Affine

properties = {
    'name': 'Affine',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
        'switch': ['encrypt', 'decrypt'],
        'a': ['1', '3', '5', '7', '9', '11', '15', '17', '19', '21', '23', '25'],
        'b': ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25'],
        '保留标点': bool
    }
}
defaults = {
    'switch': 'encrypt',
    'a': '5',
    'b': '9',
    '保留标点': False
}

def main(inp, settings):
    a = int(settings['a'])
    b = int(settings['b'])
    coder = Affine(a, b)
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0], settings['保留标点'])}
    else:
        return {0: coder.decipher(inp[0], settings['保留标点'])}
