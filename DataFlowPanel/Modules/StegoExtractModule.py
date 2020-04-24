import traceback
import subprocess
import ExternalTools.binwalk.binwalk as binwalk
import sys

properties = {
    'name': '文件隐写检查',
    'categories': '隐写',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
    }
}

defaults = {
}


def main(inp, settings):
    try:
        files = eval(inp[0])
    except Exception as e:
        files = str(inp[0])
    out = ''
    try:
        proc = subprocess.Popen(
            ['binwalk', '-e', '-M', files],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        msg = '\n\n\n\n\n\n\n\n'.encode('utf-8')
        stdout_value = proc.communicate(msg)[0].decode('utf-8')
        print(stdout_value)
    except Exception as e:
        traceback.print_exc()
        return None
    return {0: '已完成, 可提取的文件已保存至同一目录下.\n 输出:\n' + stdout_value}
