import Modules.DataFlow.BaseModuleUtils as Utils

properties = {
    'name': 'Base64隐写',
    'categories': '编码解码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
    }
}

defaults = {
}


def main(inp: dict, settings: dict):
    out = {0: Utils.base64_ste(inp[0].splitlines())}
    return out
