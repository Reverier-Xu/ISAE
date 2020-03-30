def RailFenceEncrypt(text, div):
    if div >= len(text):
        return text
    output = ''
    redivide = list()
    for i in range(0,div,1):
        redivide.append(list())
    for i in range(0,len(text),div):
        for j in range(0,div,1):
            redivide[j].append(text[i+j])
    for i in range(0,div,1):
        output += ''.join(redivide[i])
    return output


def RailFenceDecrypt(text, div):
    output = ''
    for i in range(0,len(text),1):
        
    return output
