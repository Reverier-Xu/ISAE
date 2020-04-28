import re

properties = {
    'name': '小端序拆分',
    'categories': '二进制工具',
    'input': {0: '输入'},
    'output': {0: '拆分结果'},
    'properties': {
        '前缀': str,
        '单位长度': str
    }
}

defaults = {
    '前缀': '0x',
    '单位长度': '2'
}


def main(inp, settings):
    forehead = settings['前缀']
    step = int(settings['单位长度'])
    inputs = inp[0]
    if len(inputs) % 2 != 0:
        inputs = '0' + inputs
    inputs = cut_text(inputs, step)
    out = ''
    inputs.reverse()
    for i in inputs:
        out += forehead + i
    return {0: out}


def cut_text(text, length):
    text_arr = re.findall('.{' + str(length) + '}', text)
    text_arr.append(text[(len(text_arr) * length):])
    return text_arr
