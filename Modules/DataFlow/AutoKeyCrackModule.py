from .cracks.break_autokey import break_autokey

properties = {
    'name': 'AutoKey破解',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
    }
}
defaults = {
}

def main(inp, settings):
    return {0: break_autokey(inp[0])}
