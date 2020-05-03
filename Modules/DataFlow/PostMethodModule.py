__AUTHOR__ = 'Reverier Xu'

import requests

properties = {
    'name': 'POST',
    'categories': 'Web',
    'input': {0: '地址', 1: '参数'},
    'output': {0: '应答'},
    'properties': {
        'http代理': str,
        'https代理': str,
        'time out': str
    }
}
defaults = {
    'http代理': '',
    'https代理': '',
    'time out': '1'
}


def main(inp, settings):
    timeout = int(settings['time out'])
    proxy = {}
    if settings['http代理'] != '':
        proxy['http'] = settings['http代理']
    if settings['https代理'] != '':
        proxy['https'] = settings['https代理']
    url = inp[0]
    d = eval(inp[1])
    if proxy != {}:
        r = requests.post(url, data=d, proxies=proxy, timeout=timeout)
    else:
        r = requests.post(url, data=d, timeout=timeout)
    out = {0: r.text}
    return out
