def RailFenceEncrypt(text, div):
    if div >= len(text):
        return text
    output = ''
    for i in range(0,div,1):
        output += text[i:len(text):div]
    return output


def RailFenceDecrypt(text, div):
    if div >= len(text):
        return text
    output = ''
    for i in range(0,len(text)//div+1,1):
        output += text[i:len(text):len(text)//div+1]
    return output
