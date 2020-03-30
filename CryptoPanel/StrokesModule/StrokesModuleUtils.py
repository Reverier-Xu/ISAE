def StrokesDecrypt(text):
    output = ''

    data_lines = open('Resources/汉字编码表 gbk unicode.txt', encoding='GBK').readlines()

    query_dict = {}

    # delete useless information on head
    for line in data_lines[7:]:  
        l = line.strip().split()
        unicode_mark = chr(int(l[4], 16))
        bihua = l[6]
        query_dict[unicode_mark] = bihua

    for s in text:
        output += str(query_dict.get(s, -1)) + ' '

    data_lines
    return output
