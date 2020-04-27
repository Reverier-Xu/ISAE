from Modules.DataFlow.HashModuleUtils import *

properties = {
    'name': 'MD5',
    'categories': '校验',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        'salt长度': str,
        'eval': bool,
        '是路径': bool
    }
}

defaults = {
    'salt长度': '0',
    'eval': False,
    '是路径': False
}


def main(inp, settings):
    if type(inp[0]) is str and settings['是路径']:
        return {0: str(generate_file_md5(inp[0]))}
    if settings['eval'] is True:
        inps = eval(inp[0])
    else:
        inps = inp[0].encode()
    salt = int(settings['salt长度'])
    out = {0: str(generate_md5(inps, salt))}
    return out
