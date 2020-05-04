properties = {
    'name': '圣堂武士密码',
    'categories': '密码',
    'input': {0: 'anything'},
    'output': {0: 'Image'},
    'properties': {

    }
}

defaults = {

}

def main(inp, settings):
    with open('Resources/Cipher/shengtang.png', 'rb') as img:
        out = {0: img.read()}
    return out