RailFenceListUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
RailFenceListLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def RailFenceEncrypt(text, disp):
    output = ''
    for i in range(0,len(text),1):
        if text[i] in RailFenceListUpper:
            output += RailFenceListUpper[(RailFenceListUpper.index(text[i]) + disp) % 26]
        elif text[i] in RailFenceListLower:
            output += RailFenceListLower[(RailFenceListLower.index(text[i]) + disp) % 26]
        else:
            output += text[i]
    return output


def RailFenceDecrypt(text, disp):
    output = ''
    for i in range(0,len(text),1):
        if text[i] in RailFenceListUpper:
            output += RailFenceListUpper[(RailFenceListUpper.index(text[i]) - disp) % 26]
        elif text[i] in RailFenceListLower:
            output += RailFenceListLower[(RailFenceListLower.index(text[i]) - disp) % 26]
        else:
            output += text[i]
    return output
