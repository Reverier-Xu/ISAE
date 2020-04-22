import html

properties = {
    'name': 'HTML编码',
    'categories': '编码解码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '开关': ['编码', '解码']
    }
}
defaults = {
    '开关': '编码'
}


def main(inp, settings):
    inputs = inp[0]

    if settings['开关'] == '编码':
        out = {0: html.escape(inputs)}
    else:
        out = {0: html.unescape(inputs)}
    return out
