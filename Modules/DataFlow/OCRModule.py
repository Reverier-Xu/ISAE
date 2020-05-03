__AUTHOR__ = 'Reverier Xu'

from aip import AipOcr

properties = {
    'name': '百度-OCR',
    'categories': 'AI',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        'APP_ID': str,
        'API_KEY': str,
        'SECRECT_KEY': str,
        '高精度': bool,
        '注': str
    }
}

defaults = {
    'APP_ID': '',
    'API_KEY': '',
    'SECRECT_KEY': '',
    '高精度': False,
    '注': '此功能需要您自行前往https://console.bce.baidu.com/ai/ 申请API接口才可使用. 申请是免费的, 并且很迅速.'
}


def main(inp, settings):
    """利用百度api识别文本，并保存提取的文字
    picfile:    图片文件名
    outfile:    输出文件
    """

    client = AipOcr(settings['APP_ID'],
                    settings['API_KEY'], settings['SECRECT_KEY'])

    img = eval(inp[0])
    if settings['高精度']:
        message = client.basicAccurate(img)  # 通用文字高精度识别，每天 800 次免费
    else:
        message = client.basicGeneral(img)  # 通用文字识别，每天 50 000 次免费
    print("识别成功！")

    fo = ''
    # 输出文本内容
    for text in message.get('words_result'):
        fo += text.get('words')
    return {0: fo}
