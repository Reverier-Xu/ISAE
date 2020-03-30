CaesarListUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
CaesarListLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def CaesarEncrypt(text, disp):
    output = ''
    for i in range(0,len(text),1):
        if text[i] in CaesarListUpper:
            output += CaesarListUpper[(CaesarListUpper.index(text[i]) + disp) % 26]
        elif text[i] in CaesarListLower:
            output += CaesarListLower[(CaesarListLower.index(text[i]) + disp) % 26]
        else:
            output += text[i]
    return output


def CaesarDecrypt(text, disp):
    output = ''
    for i in range(0,len(text),1):
        if text[i] in CaesarListUpper:
            output += CaesarListUpper[(CaesarListUpper.index(text[i]) - disp) % 26]
        elif text[i] in CaesarListLower:
            output += CaesarListLower[(CaesarListLower.index(text[i]) - disp) % 26]
        else:
            output += text[i]
    return output
