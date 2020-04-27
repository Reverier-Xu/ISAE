import traceback

properties = {
    'name': '排序',
    'categories': '小工具',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '分割符': str,
        '行排序': bool,
        '从大到小': bool,
        '数字': bool
    }
}

defaults = {
    '分割符': ' ',
    '行排序': False,
    '从大到小': False,
    '数字': False
}


def main(inp, settings):
    try:
        data = inp[0]
        if settings['行排序']:
            data = data.splitlines()
            if settings['数字']:
                for i in range(len(data)):
                    try:
                        data[i] = int(data[i])
                    except BaseException:
                        data.remove(data[i])
            data = sorted(data, reverse=settings['从大到小'])
            for i in range(len(data)):
                data[i] = str(data[i])
            return {0: '\n'.join(data)}

        data = data.split(settings['分割符'])
        if settings['数字']:
            for i in range(len(data)):
                try:
                    data[i] = int(data[i])
                except BaseException:
                    data.remove(data[i])
        data = sorted(data, reverse=settings['从大到小'])
        for i in range(len(data)):
            data[i] = str(data[i])
        data = settings['分割符'].join(data)
        return {0: data}
    except BaseException:
        traceback.print_exc()
