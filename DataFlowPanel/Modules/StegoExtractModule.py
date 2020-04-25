import traceback
import binwalk

properties = {
    'name': '文件隐写检查',
    'categories': '隐写',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        '注': str,
    }
}

defaults = {
    '注': '建议提取时, 保证ICTFE的母终端处于打开状态. 某些文件提取时可能会需要手动在终端中回车.'
}


def main(inp, settings):
    try:
        files = eval(inp[0])
    except Exception as e:
        files = str(inp[0])
    out = ''
    try:
        for module in binwalk.scan(files, quiet=False, extract=True, signature=True):
            for result in module.results:
                out += ("Extracted '%s' at offset 0x%X" % (result.description.split(',')[0],
                                                           result.offset) + '\n')
    except Exception as e:
        traceback.print_exc()
        return None
    return {0: '已完成, 可提取的文件已保存至同一目录下.\n 输出:\n' + out}
