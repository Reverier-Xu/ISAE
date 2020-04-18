CaesarListUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
CaesarListLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
CaesarDigit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def CaesarEncrypt(text, disp, digit=False, step=0, limit=26):
    output = ''
    for i in range(0, len(text), 1):
        if text[i] in CaesarListUpper:
            output += CaesarListUpper[(CaesarListUpper.index(text[i]) + disp) % limit]
            disp += step
        elif text[i] in CaesarListLower:
            output += CaesarListLower[(CaesarListLower.index(text[i]) + disp) % limit]
            disp += step
        elif text[i] in CaesarDigit and digit:
            output += CaesarDigit[(CaesarDigit.index(text[i]) + disp) % 10]
        else:
            output += text[i]
    return output


def CaesarDecrypt(text, disp, digit=False, step=0, limit=26):
    output = ''
    for i in range(0, len(text), 1):
        if text[i] in CaesarListUpper:
            output += CaesarListUpper[(CaesarListUpper.index(text[i]) - disp) % limit]
            disp += step
        elif text[i] in CaesarListLower:
            output += CaesarListLower[(CaesarListLower.index(text[i]) - disp) % limit]
            disp += step
        elif text[i] in CaesarDigit and digit:
            output += CaesarDigit[(CaesarDigit.index(text[i]) - disp) % 10]
        else:
            output += text[i]
    return output
