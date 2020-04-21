import re

properties = {
    'name': '分隔符添加',
    'categories': '字符串操作',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '分隔符': str,
        '长度': str
    }
}

defaults = {
    '分隔符': '',
    '长度': '1'
}


def main(inp, settings):
    out = {0: settings['分隔符'].join(cut_text(inp[0], int(settings['长度'])))}
    return out


def cut_text(text, lenth):
    textArr = re.findall('.{' + str(lenth) + '}', text)
    textArr.append(text[(len(textArr) * lenth):])
    return textArr
