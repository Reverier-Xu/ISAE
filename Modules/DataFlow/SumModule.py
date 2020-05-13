properties = {
    'name': 'sum',
    'categories': '数学工具',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {}
}

defaults = {}


def main(inp, settings):
    nums = inp[0].split(' ')
    for i in range(len(nums)):
        try:
            nums[i] = int(nums[i])
        except:
            pass
    out = 0
    for i in nums:
        try:
            out += i
        except:
            pass
    return {0: str(out)}
