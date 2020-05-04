from Crypto.Cipher import ARC4
from binascii import b2a_hex, a2b_hex

def myRC4(data,key):
    rc41 = ARC4.new(key)
    encrypted = rc41.encrypt(data)
    return encrypted.encode('hex')

def rc4_decrpt_hex(data,key):
    rc41=ARC4.new(key)
    return rc41.decrypt(a2b_hex(data))

properties = {
    'name': 'RC4',
    'categories': '密码',
    'input': {0: 'input', 1: 'key'},
    'output': {0: '输出'},
    'properties': {
        'switch': ['encrypt', 'decrypt']
    }
}

defaults = {'switch': 'encrypt'}

def main(inp, settings):
    if settings['switch'] == 'encrypt':
        return {0:myRC4(inp[0], inp[1])}
    else:
        return {0: rc4_decrpt_hex(inp[0], inp[1])}
