MorseList = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
    "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
    "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

    ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
    "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
    "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
    ".--.-.": "@", ".-.-.": "+", ".......":" ",
}


def MorseEncode(text, spilt):
    output = ''
    lists = list(MorseList.values())
    print(lists)
    for i in text.upper():
        output += list(MorseList.keys())[lists.index(i)]
        output += spilt
    output = output[:-len(spilt)]
    return output


def MorseDecode(text, spilt):
    print(text)
    temp = text.split(spilt)
    print(temp)
    output = ''
    for i in temp:
        output += MorseList[i]
    return output
