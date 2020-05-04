from .cracks.break_fracmorse import break_fracmorse

properties = {
    'name': 'FracMorse破解',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
    }
}
defaults = {
}

def main(inp, settings):
    return {0: break_fracmorse(inp[0])}
