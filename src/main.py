import random
from examples import expls

from utils import colors as clrs
from utils.colors import clr
from utils.colors import Color

from utils import tools as tls
from utils.tools import N
from utils.debug import TEST

def generate_rand_sdk():
    sdk = []
    for i in range(9):
        row = []
        for i in range(9):
            n = random.randint(1, 9)
            row.append(n)
        sdk.append(row) 
    return sdk

def get_kwargs(defaults, **kwargs):
    ret = {}
    for key, value in defaults.items():
        ret[key] = value if key not in kwargs else kwargs[key]
    return ret

def get_args_from_kwargs(**kwargs):
    sep = get_kwargs({'vert': '|', 'horz': '-', 'cross': '+'}, **kwargs)
    sep_clr = Color.BRIGHT_BLUE if 'sep_clr' not in kwargs else kwargs['sep_clr']
    txt_clr = Color.BRIGHT_BLACK if 'clr' not in kwargs else kwargs['clr']
    return {**clrs.clr_dict(sep, sep_clr), 'clr': txt_clr}

def sdk_to_l_str(sdk, **kwargs):
    args = get_args_from_kwargs(**kwargs)

    cp = ['' for _ in range(11)]
    off = 0
    for i, l in enumerate(sdk):
        if i == 3 or i == 6:
            for j in range(19): 
                cp[i + off] += args['horz']
                if j == 5 or j == 12:
                    cp[i + off] += args['cross']
            off += 1
        for x, n in enumerate(l):
            space = ' ' if x < len(l) - 1 else ''
            # space = ' '
            cp[i + off] += clr(str(n) + space, args['clr'])
            if x == 2 or x == 5:
                cp[i + off] += args['vert'] + clr(' ', args['clr'])
    return cp

def print_sdk(sdk, indent=2, marg_top=1, marg_bot=1, **kwargs):
    s = sdk_to_l_str(sdk, **kwargs)        
    print('\n' * marg_top, end='')
    for l in s:
        print(indent * ' ', l, sep='')
    print('\n' * marg_bot, end='')
        
def print_simple_sdk(sdk):
    for i, l in enumerate(sdk):
        print(*l, sep=' | ')
        if i != len(sdk) - 1:
            print_sep()

def find_all_in(items, l):
    for i, item in enumerate(items):
        if item not in l:
            return i
    return -1

def is_valid_sdk(sdk):
    range_9 = [i + 1 for i in range(9)]
    for i, l in enumerate(sdk):
        ret = find_all_in(range_9, l)
        if ret != -1:
            print(f'row: {i + 1}, number not in row: {ret + 1}')
            return False

    for y in range(9):
        col = [sdk[x][y] for x in range(9)]
        ret = find_all_in(range_9, col)
        if ret != -1:
            print(f'col: {y + 1}, number not in row: {ret + 1}')
            return False

    for i in range(9):
        square = [sdk[i - i % 3 + x][(i * 3) % 9 + y] for y in range(3) for x in range(3)]
        ret = find_all_in(range_9, square)
        if ret != -1:
            print(f'square: {i}, number not in square: {ret + 1}')
            return False
    return True

def print_res(bool):
    if bool:
        print("Good sudoku")
    else:
        print("Bad sudoku")

def print_sep(n=33, sep='-'):
    print(sep * n)

def init_main():
    pass

def exit_main():
    pass

def main():
    sdk = generate_rand_sdk()

    print_sdk(sdk, 5, 3, 3, 
              vert='|',
              horz='=',
              cross='x',
              sep_clr=clrs.get_256_clr_code(167),
              clr=clrs.get_256_bg_clr_code(95)+clrs.get_256_clr_code(230))
    print_res(is_valid_sdk(sdk))
    sdk = expls.bad_square_exple()
    
    print_sdk(sdk, 5, 3, 3)
    print_res(is_valid_sdk(sdk))
    N()
    
    # clrs.list_256_clrs()
    
if __name__ == "__main__":
    main()
    
