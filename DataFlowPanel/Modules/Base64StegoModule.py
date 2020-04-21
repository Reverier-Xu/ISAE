import DataFlowPanel.Modules.BaseModuleUtils as utils

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
    out = {}
    out[0] = utils.base64_ste(inp[0].splitlines())
    return out
