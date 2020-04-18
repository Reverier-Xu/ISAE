import binascii


def hex2char(data):
    output = binascii.unhexlify(data.encode())
    return output


def char2hex(data):
    output = binascii.hexlify(data.encode())
    return output
