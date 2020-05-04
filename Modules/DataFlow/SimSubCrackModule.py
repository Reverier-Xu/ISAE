from .cracks.break_simplesub import break_simplesub

properties = {
    'name': '词频分析(慢)',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
    }
}
defaults = {
}

def main(inp, settings):
    return {0: break_simplesub(inp[0])}
