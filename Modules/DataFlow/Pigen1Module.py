properties = {
    'name': '猪圈密码（变种1）',
    'categories': '密码',
    'input': {0: 'anything'},
    'output': {0: 'Image'},
    'properties': {

    }
}

defaults = {
}

def main(inp, settings):
    with open('Resources/Cipher/pigen-1.jpg', 'rb') as img:
        out = {0: img.read()}
    return out