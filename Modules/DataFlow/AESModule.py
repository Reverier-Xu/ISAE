from Crypto.Cipher import AES
import math

properties = {
    'name': 'AES',
    'categories': '密码',
    'input': {0: 'cipher', 1: 'key'},
    'output': {0: '输出'},
    'properties': {
        'mode': ['CBC', 'ECB', 'CFB', 'OFB', 'CTR', 'OCB', 'SIV', 'GCM', 'EAX', 'CCM', 'OPENPGP'],
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
        mode = AES.MODE_CBC
    elif settings['mode'] == 'ECB':
        mode = AES.MODE_ECB
    elif settings['mode'] == 'CFB':
        mode = AES.MODE_CFB
    elif settings['mode'] == 'OFB':
        mode = AES.MODE_OFB
    elif settings['mode'] == 'CTR':
        mode = AES.MODE_CTR
    elif settings['mode'] == 'OCB':
        mode = AES.MODE_OCB
    elif settings['mode'] == 'SIV':
        mode = AES.MODE_SIV
    elif settings['mode'] == 'GCM':
        mode = AES.MODE_GCM
    elif settings['mode'] == 'EAX':
        mode = AES.MODE_EAX
    elif settings['mode'] == 'CCM':
        mode = AES.MODE_CCM
    elif settings['mode'] == 'OPENPGP':
        mode = AES.MODE_OPENPGP
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
    aes_obj = AES.new(key, mode, iv)
    padding_zero=pad(text)
    e_buf=aes_obj.encrypt(padding_zero)
    return e_buf

def decrypt(buff, key, iv, mode):
    aes_obj = AES.new(key, mode, iv)
    text=aes_obj.decrypt(buff)
    return text

