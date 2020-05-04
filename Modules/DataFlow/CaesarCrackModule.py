from .cracks.break_caesar import break_caesar

properties = {
    'name': 'Caesar破解',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
    }
}
defaults = {
}

def main(inp, settings):
    return {0: break_caesar(inp[0])}
