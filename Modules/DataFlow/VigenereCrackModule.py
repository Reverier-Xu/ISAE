from .cracks.break_vigenere import break_vigenere

properties = {
    'name': 'Vigenere破解',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
    }
}
defaults = {
}

def main(inp, settings):
    return {0: break_vigenere(inp[0])}
