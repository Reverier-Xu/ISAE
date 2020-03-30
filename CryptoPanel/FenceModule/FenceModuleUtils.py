FenceListUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
FenceListLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def FenceEncrypt(text, disp):
    output = ''
    for i in range(0,len(text),1):
        if text[i] in FenceListUpper:
            output += FenceListUpper[(FenceListUpper.index(text[i]) + disp) % 26]
        elif text[i] in FenceListLower:
            output += FenceListLower[(FenceListLower.index(text[i]) + disp) % 26]
        else:
            output += text[i]
    return output


def FenceDecrypt(text, disp):
    output = ''
    for i in range(0,len(text),1):
        if text[i] in FenceListUpper:
            output += FenceListUpper[(FenceListUpper.index(text[i]) - disp) % 26]
        elif text[i] in FenceListLower:
            output += FenceListLower[(FenceListLower.index(text[i]) - disp) % 26]
        else:
            output += text[i]
    return output
