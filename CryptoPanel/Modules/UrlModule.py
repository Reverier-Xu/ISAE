from urllib import parse

properties = {
    'name': 'Url编码',
    'categlories': '编码解码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '开关': ['编码', '解码'],
        '编码表': str,
        'all': bool
    }
}

defaults = {
    '开关': '编码',
    '编码表': 'UTF-8',
    'all': False
}


def main(inp: dict, settings: dict):
    out = {}
    if settings['开关'] == '编码':
        if settings['all']:
            cipher = ''
            for i in inp[0]:
                if 127 >= ord(i) >= 0:
                    cipher += '%{:02X}'.format(ord(i))
                else:
                    cipher += parse.quote(i, encoding=settings['编码表'])
            out[0] = cipher
        else:
            out[0] = parse.quote(inp[0], encoding=settings['编码表'])
    elif settings['开关'] == '解码':
        out[0] = parse.unquote(inp[0], encoding=settings['编码表'])
    return out
