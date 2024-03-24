import random
import time

from utils import colors as clrs
from utils.colors import clr
from utils.colors import Color

from utils import tools as tls
from utils.tools import N
from utils.debug import TEST
from utils import rgx
from utils import data_stuct as ds

from examples import expls

from sdk import sdk
from sdk.sdk import Sdk
from sdk.sdk import NewGrid
from sdk import style as module_style
from sdk.style import Style

# =============================================================================
# Generate
# =============================================================================


def generate_rand_sdk():
    sdk = []
    for i in range(9):
        row = []
        for i in range(9):
            n = random.randint(1, 9)
            row.append(n)
        sdk.append(row) 
    return sdk


# =============================================================================
# Check if sudoku is valid
# =============================================================================


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

def is_valid_sdk_2(sdk):
    # print(sdk)
    sdk = ds.apply_funcs_to_lists(sdk, [clrs.rm_clr, int], [None])
    # print(sdk)
    # time.sleep(10)
    for i, l in enumerate(sdk):
        if ds.has_duplicates(l, [None]):
            # print(i, l, '\nligne FALSE')
            return False
        # else:
        #     print(l)

    for y in range(9):
        col = [sdk[x][y] for x in range(9)]
        if ds.has_duplicates(col, [None]):
            # print(i, col, '\ncol FALSE')
            return False

    for i in range(9):
        square = [sdk[i - i % 3 + x][(i * 3) % 9 + y] for y in range(3) for x in range(3)]
        if ds.has_duplicates(square, [None]):
            # print(i, col, '\nsquare FALSE')
            return False

    return True

# =============================================================================
# Print sudoku in terminal
# =============================================================================


def print_sdk(sdk, **kwargs):
    format = tls.get_kwargs({'indent': 2, 'top_margin': 1, 'bot_margin': 1}, **kwargs)
    s = sdk_to_l_str(sdk, **kwargs)        
    print('\n' * format['top_margin'], end='')
    for l in s:
        print(format['indent'] * ' ', l, sep='')
    print('\n' * format['bot_margin'], end='')
        
def print_simple_sdk(sdk):
    for i, l in enumerate(sdk):
        print(*l, sep=' | ')
        if i != len(sdk) - 1:
            print_sep()

def print_res(bool):
    if bool:
        print("Good sudoku")
    else:
        print("Bad sudoku")

def print_sep(n=33, sep='-'):
    print(sep * n)



# =============================================================================
# Convert
# =============================================================================


def get_args_from_kwargs(**kwargs):
    sep = tls.get_kwargs({'vert': '|', 'horz': '-', 'cross': '+'}, **kwargs)
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
            if n == None:
                value = clr(' ', clrs.get_256_bg_clr_code(95))
            else:
                value = str(n)
            space = ' ' if x < len(l) - 1 else ''
            # space = ' '
            cp[i + off] += clr(value + space, args['clr'])
            if x == 2 or x == 5:
                cp[i + off] += args['vert'] + clr(' ', args['clr'])
    return cp


# =============================================================================
# Other
# =============================================================================

def str_to_sdk(text, empty='.', replace=None, size=3):
    l = rgx.extract_numbers_and_chars(text, empty)
    ds.replace_in_nested_lists(l, empty, replace)
    chunked = ds.chunk_list(l, size * size)
    return chunked

def modif_sdk(sdk, coord, new_value):
    new_value = None if new_value == None else clr(str(new_value), clrs.get_256_bg_clr_code(219) + Color.BLACK + Color.BOLD)
    sdk[coord[1]][coord[0]] = new_value

def increment_2d(coord, inc, size_x, size_y):
    x = (coord[0] + inc) % size_x
    y = coord[1] + (coord[0] + inc) // size_x
    if x > size_x - 1 or y > size_y - 1:
        return False
    return (x, y)            
 
def solve_sdk(sdk):
    # print_sdk(sdk, **style['wood'])
    
    coord = (0, 0)
    coord = ds.find_from_in_2d_list(sdk, None, coord)
    if coord == False:
        print("\n" + clr('-------SUCCESS------', Color.BRIGHT_GREEN) + "\n")
        return True
    
    for i in range(9):
        modif_sdk(sdk, coord, i + 1)
        
        tls.clear_screen()
        
        print_sdk(sdk)
        ret = is_valid_sdk_2(sdk)
        time.sleep(0.0005)
        

        if ret == True:
            if solve_sdk(sdk) == True:
                return True
            
    modif_sdk(sdk, coord, None)
    return False


# =============================================================================
# Main
# =============================================================================


def init_main():
    pass

def exit_main():
    pass


def main():
    
    text = '''
            sudoku_puzzle = [
            [5, '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', 7, '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 8, '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', 7, '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 5, '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', 4, '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 2, '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', 3, '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', 9]
            ]
            '''
    
    new_sdk = NewGrid(text)
    grid = new_sdk.str_to_grid()
    
    sdk = Sdk(grid, Style(**module_style.styles['my_style']))
    sdk.show_simple()
    
    # sdk = str_to_sdk(text, '0')
    # print_sdk(sdk)
    # solve_sdk(sdk)
    return
    
if __name__ == "__main__":
    main()

