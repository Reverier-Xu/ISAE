__AUTHOR__ = 'Reverier Xu'


def ROT13(text):
    rot13 = str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    output = text.translate(rot13)
    return output


def ROT47(s):
    x = []
    for i in range(0, len(s), 1):
        j = ord(s[i])
        if 33 <= j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)
