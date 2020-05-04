from Crypto.Cipher import DES
import math

properties = {
    'name': 'DES',
    'categories': '密码',
    'input': {0: 'cipher', 1: 'key'},
    'output': {0: '输出'},
    'properties': {
        'mode': ['CBC', 'ECB', 'CFB', 'OFB', 'CTR', 'OCB', 'EAX', 'OPENPGP'],
        'iv': str,
        'switch': ['encrypt', 'decrypt']
    }
}

defaults = {
    'mode': 'CBC',
    'iv': "68b329da9893e34099c7d8ad5cb9c940",
    'switch': 'encrypt'
}

def main(inp, settings):
    key = parse_hex(inp[1])
    text = inp[0]
    iv = parse_hex(settings['iv'])
    if settings['mode'] == 'CBC':
        mode = DES.MODE_CBC
    elif settings['mode'] == 'ECB':
        mode = DES.MODE_ECB
    elif settings['mode'] == 'CFB':
        mode = DES.MODE_CFB
    elif settings['mode'] == 'OFB':
        mode = DES.MODE_OFB
    elif settings['mode'] == 'CTR':
        mode = DES.MODE_CTR
    elif settings['mode'] == 'OCB':
        mode = DES.MODE_OCB
    elif settings['mode'] == 'EAX':
        mode = DES.MODE_EAX
    elif settings['mode'] == 'OPENPGP':
        mode = DES.MODE_OPENPGP
    if settings['switch'] == 'encrypt':
        out = {0: encrypt(text, key, iv, mode)}
    else:
        out = {0: decrypt(text, key, iv, mode)}

    return out

# padding算法，原理就是按照16字节对齐
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(0) 
unpad = lambda s : s[0:-ord(s[-1])]

def parse_hex(hex_str):
    l=int(math.ceil(len(hex_str)/2))
    buf=''
    for i in range(0,l):
        s=hex_str[(i*2):((i+1)*2)]
        buf=buf+chr(int(s,16))
    return buf

def encrypt(text, key, iv, mode):
    DES_obj = DES.new(key, mode, iv)
    padding_zero=pad(text)
    e_buf=DES_obj.encrypt(padding_zero)
    return e_buf

def decrypt(buff, key, iv, mode):
    DES_obj = DES.new(key, mode, iv)
    text=DES_obj.decrypt(buff)
    return text

