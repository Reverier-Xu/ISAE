
def bf(src, left, right, data, idx):
    """
        brainfuck interpreter
        src: source string
        left: start index
        right: ending index
        data: input data string
        idx: start-index of input data string
    """
    out = ''
    if len(src) == 0: return
    if left < 0: left = 0
    if left >= len(src): left = len(src) - 1
    if right < 0: right = 0
    if right >= len(src): right = len(src) - 1
    # tuning machine has infinite array size
    # increase or decrease here accordingly
    arr = [0] * 30000
    ptr = 0
    i = left
    while i <= right:
        s = src[i]
        if s == '>':
            ptr += 1
            # wrap if out of range
            if ptr >= len(arr):
                ptr = 0
        elif s == '<':
            ptr -= 1
            # wrap if out of range
            if ptr < 0:
                ptr = len(arr) - 1
        elif s == '+':
            arr[ptr] += 1
        elif s == '-':
            arr[ptr] -= 1
        elif s == '.':
            out += chr(arr[ptr])
        elif s == ',':
            if idx >= 0 and idx < len(data):
                arr[ptr] = ord(data[idx])
                idx += 1
            else:
                arr[ptr] = 0 # out of input
        elif s =='[':
            if arr[ptr] == 0:
                loop = 1
                while loop > 0:
                    i += 1
                    c = src[i]
                    if c == '[':
                        loop += 1
                    elif c == ']':
                        loop -= 1
        elif s == ']':
            loop = 1
            while loop > 0:
                i -= 1
                c = src[i]
                if c == '[':
                    loop -= 1
                elif c == ']':
                    loop += 1
            i -= 1
        i += 1
    return out
properties = {
    'name': 'brainfuck',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties':{}
}
defaults={}
def main(inp, settings):
    return {0:bf(inp[0], 0, len(inp[0]) - 1, "", 0)}