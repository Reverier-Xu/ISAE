# -*- coding:utf-8 -*-
from base64 import *


Base64StandardTable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
Base32StandardTable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
Base16StandardTable = '0123456789ABCDEF'
Base85StandardTable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#'
Base85ReverseTable = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'


def base64_ste(lines):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    flag = ''
    temp = 0
    digit = 0
    for i in lines:
        if i[-1] != '=':
            continue
        elif i[-2] != '=':
            digit += 2
            temp = (temp << 2) + (alphabet.find(i[-2]) & 0x3)
        else:
            digit += 4
            temp = (temp << 4) + (alphabet.find(i[-3]) & 0xf)
        if digit == 8:
            digit = 0
            flag += chr(temp)
            temp = 0
        elif digit > 8:
            digit = 2
            flag += chr(temp >> 2)
            temp = temp & 0x3
    return flag


def ChangeTableBase64Decode(cipher, new_table):
    old_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    trans = str.maketrans(new_table, old_table)
    cipher = cipher.translate(trans)
    text = ''
    try:
        text = b64decode(cipher.encode()).decode()
    except:
        text = b64decode(cipher.encode())
    return text


def ChangeTableBase64Encode(text, new_table, flag=False):
    if flag == True:
        cipher = b64encode(eval(text)).decode()
    else:
        cipher = b64encode(text.encode()).decode()
    old_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    trans = str.maketrans(old_table, new_table)
    cipher = cipher.translate(trans)
    return cipher


def ChangeTableBase32Decode(cipher, new_table):
    old_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
    trans = str.maketrans(new_table, old_table)
    cipher = cipher.translate(trans)
    text = ''
    try:
        text = b32decode(cipher.encode()).decode()
    except:
        text = b32decode(cipher.encode())
    return text


def ChangeTableBase32Encode(text, new_table, flag=False):
    if flag == True:
        cipher = b32encode(eval(text)).decode()
    else:
        cipher = b32encode(text.encode()).decode()
    old_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
    trans = str.maketrans(old_table, new_table)
    cipher = cipher.translate(trans)
    return cipher


def ChangeTableBase16Decode(cipher, new_table):
    old_table = '0123456789ABCDEF'
    trans = str.maketrans(new_table, old_table)
    cipher = cipher.translate(trans)
    text = ''
    try:
        text = b16decode(cipher.encode()).decode()
    except:
        text = b16decode(cipher.encode())
    return text


def ChangeTableBase16Encode(text, new_table, flag=False):
    if flag == True:
        cipher = b16encode(eval(text)).decode()
    else:
        cipher = b16encode(text.encode()).decode()
    old_table = '0123456789ABCDEF'
    trans = str.maketrans(old_table, new_table)
    cipher = cipher.translate(trans)
    return cipher


def ChangeTableBase85Decode(cipher, new_table):
    old_table = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#"
    trans = str.maketrans(new_table, old_table)
    cipher = cipher.translate(trans)
    text = ''
    try:
        text = a85decode(cipher.encode()).decode()
    except:
        text = a85decode(cipher.encode())
    return text


def ChangeTableBase85Encode(text, new_table, flag=False):
    if flag == True:
        cipher = b85encode(eval(text)).decode()
    else:
        cipher = b85encode(text.encode()).decode()
    old_table = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#"
    trans = str.maketrans(old_table, new_table)
    cipher = cipher.translate(trans)
    return cipher


def ChangeTableBase85RFCEncode(text, new_table, flag=False):
    if flag == True:
        cipher = b85encode(eval(text)).decode()
    else:
        cipher = b85encode(text.encode()).decode()
    old_table = Base85ReverseTable
    trans = str.maketrans(old_table, new_table)
    cipher = cipher.translate(trans)
    return cipher


def ChangeTableBase85RFCDecode(cipher, new_table):
    old_table = Base85ReverseTable
    trans = str.maketrans(new_table, old_table)
    cipher = cipher.translate(trans)
    text = ''
    try:
        text = b85decode(cipher.encode()).decode()
    except:
        text = b85decode(cipher.encode())
    return text


def Base64FileEncode(InputPath, OutputPath):
    f = open(InputPath, "r")
    inp = f.read()
    outp = open(OutputPath, "wb")
    outp.write(b64encode(inp.encode()))


def Base64FileDecode(InputPath, OutputPath):
    f = open(InputPath, "r")
    inp = f.read()
    outp = open(OutputPath, "wb")
    outp.write(b64decode(inp.encode()))


def Base32FileEncode(InputPath, OutputPath):
    f = open(InputPath, "r")
    inp = f.read()
    outp = open(OutputPath, "wb")
    outp.write(b32encode(inp.encode()))


def Base32FileDecode(InputPath, OutputPath):
    f = open(InputPath, "r")
    inp = f.read()
    outp = open(OutputPath, "wb")
    outp.write(b32decode(inp.encode()))


def Base16FileEncode(InputPath, OutputPath):
    f = open(InputPath, "r")
    inp = f.read()
    outp = open(OutputPath, "wb")
    outp.write(b16encode(inp.encode()))


def Base16ileDecode(InputPath, OutputPath):
    f = open(InputPath, "r")
    inp = f.read()
    outp = open(OutputPath, "wb")
    outp.write(b16decode(inp.encode()))


def Base85FileEncode(InputPath, OutputPath):
    f = open(InputPath, "r")
    inp = f.read()
    outp = open(OutputPath, "wb")
    outp.write(a85encode(inp.encode()))


def Base85FileDecode(InputPath, OutputPath):
    f = open(InputPath, "r")
    inp = f.read()
    outp = open(OutputPath, "wb")
    outp.write(a85decode(inp.encode()))


def Base85RFCFileEncode(InputPath, OutputPath):
    f = open(InputPath, "r")
    inp = f.read()
    outp = open(OutputPath, "wb")
    outp.write(a85encode(inp.encode()))


def Base85RFCFileDecode(InputPath, OutputPath):
    f = open(InputPath, "r")
    inp = f.read()
    outp = open(OutputPath, "wb")
    outp.write(a85decode(inp.encode()))
