properties = {
    'name': '按表翻译',
    'categories': '字符串工具',
    'input': {0: '目标表', 1: '密文表', 2: '密文'},
    'properties': {}
}
defaults = {}


def main(inp, settings):
    return {0: changetable(inp[0], inp[1], inp[2])}


def changetable(targettable, ciphertable, cipher):
    res = ""
    for i in range(len(cipher)):
        for j in range(len(ciphertable)):
            if cipher[i] == ciphertable[j]:
                res += targettable[j]
                break
    return res
