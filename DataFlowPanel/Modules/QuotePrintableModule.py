import binascii
import traceback

properties = {
    'name': 'Quoted Printable',
    'categories': '编码解码',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '开关': ['编码', '解码'],
        'eval': bool
    }
}

defaults = {
    '开关': '编码',
    'eval': False
}

def main(inp, settings):
    inputs = inp[0]
    if settings['eval'] == True:
        inputs = eval(inputs)
    else:
        inputs = inputs.encode()
    if settings['开关'] == '编码':
        outputs = binascii.b2a_qp(inputs)
    else:
        try:
            outputs = binascii.a2b_qp(inputs)
        except:
            error = traceback.format_exc()
            raise Exception(error)
    print(outputs)
    out = {0: outputs}
    return out
