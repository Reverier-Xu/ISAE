import requests

properties = {
    'name': 'GET',
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
    r = url + '?'
    for i in d:
        r += i + '=' + d[i] + '&'
    if proxy != {}:
        r = requests.get(r, proxies=proxy, timeout=timeout)
    else:
        r = requests.get(r, timeout=timeout)
    out = {0: r.text}
    return out
