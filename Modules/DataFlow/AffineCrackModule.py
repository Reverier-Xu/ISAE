from .cracks.break_affine import break_affine

properties = {
    'name': 'Affine破解',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
    }
}
defaults = {
}

def main(inp, settings):
    return {0: break_affine(inp[0])}
