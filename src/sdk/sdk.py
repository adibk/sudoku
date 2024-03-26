import time
import random

from utils import calculus as cal
from utils import tools as tls
from utils import rgx
from utils import data_stuct as ds

from utils import colors as clrs
from utils.colors import clr
from utils.colors import Color

import sdk.style as module_style
from sdk.style import Style
from examples import expls


# =============================================================================
#  Grid
# =============================================================================


class Grid():
    def __init__(self, input=None, empty_text='0', empty_lines=None):
        self._text = None
        self._lines = None
        self._size = None
        self._length = None
        self._empty_text = None
        self._empty_lines = None
        
        self.set_empty_text(empty_text)
        self.set_empty_lines(empty_lines)
        
        if isinstance(input, str):
            self.text = input
        elif isinstance(input, list):
            self.lines = input
        elif input != None:
            error_msg = (
                f"{self.__class__.__name__}.{self.__init__.__name__} "
                f"expects a string or a list to create an instance of "
                f"{self.__class__.__name__}, "
                f"got {type(input).__name__} instead."
            )
            raise TypeError(error_msg)

        
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, new_text):
        self._text = new_text
        self.set_lines(self.str_to_lines(new_text))
    
    @property
    def lines(self):
        return self._lines
    
    @property
    def size(self):
        return self._size
    
    @lines.setter
    def lines(self, new_lines):
        self.replace_in_lines(new_lines)
        self.set_lines(new_lines)
        self._text = None
        
    @property
    def length(self):
        return self._length
    
    @property
    def empty_text(self):
        return self._empty_text

    @empty_text.setter
    def empty_text(self, new_empty_text):
        self.set_empty_text(new_empty_text)
    
    @property
    def empty_lines(self):
        return self._empty_lines
                
    @empty_lines.setter
    def empty_lines(self, new_empty_lines):
        self.set_empty_lines(new_empty_lines)
    
    def set_lines(self, new_lines):
        # print('set_lines')
        length = len(new_lines)
        error_msg = (
            f"{self.__class__.__name__}.{self.set_lines.__name__} "
            f"expects a list of lists, length X * X"
        )
        
        if not length > 1 or not cal.is_perfect_sqrt(length):
            raise ValueError(error_msg)
        for line in new_lines:
            if not isinstance(line, list) or length != len(line):
                raise ValueError(error_msg)
        
        self._lines = new_lines
        self.set_size_length()

    def is_number_not_zero(self, s):
        if s == None:
            return False
        try:
            num = int(s)
            return num != 0
        except ValueError:
            return False

    def check_if_nb(self, s, name):
        if self.is_number_not_zero(s):
            raise ValueError(f'`{name}` cannot be [1-9]')

    def set_empty_text(self, empty_text):
        # print('set empty_text')
        if not isinstance(empty_text, str):
            error_msg = (
                f"{self.__class__.__name__}.{self.set_empty_text.__name__} "
                f"expects a str, "
                f"got {type(empty_text).__name__} instead."
            )
            raise TypeError(error_msg)
        self.check_if_nb(empty_text, 'empty_text')
        self._empty_text = empty_text
            
    def set_empty_lines(self, empty_lines):
        # print('set empty_line')
        self.check_if_nb(empty_lines, 'empty_lines')
        self._empty_lines = empty_lines
        if self.lines != None:
            self.replace_in_lines(self._lines)
    
    def set_size_length(self):
        # print('set_size_length')
        if self.lines != None:
            self._size = cal.perfect_sqrt(len(self.lines))
            self._length = self._size * self._size

    def lines_to_str_status(self):
        return '\n'.join(str(sublist) for sublist in self.lines)
    
    def status(self, text_clr=Color.BRIGHT_BLUE):
        status = (
            f"{clr('Text', text_clr)}\n{str(self.text)}\n\n"
            f"{clr('Lines', text_clr)}\n{str(self.lines_to_str_status())}\n\n"
            f"{clr('Size: ', text_clr):<30}{str(self.size)}\n"
            f"{clr('Length: ', text_clr):<30}{str(self.length)}\n"
            f"{clr('Empty_text: ', text_clr):<30}{str(self.empty_text)}\n"
            f"{clr('Empty_lines: ', text_clr):<30}{str(self.empty_lines)}\n"
        )
        return status
    
    def show_status(self, text_clr=Color.BRIGHT_BLUE):
        print(self.status(text_clr))

    def replace_in_lines(self, lines):
        ds.replace_others_in_nestlists(lines, [i for i in range(1, 10)], self.empty_lines)
    
    def guess_size(self, list_):
        return cal.perfect_sqrt(cal.perfect_sqrt(len(list_)))
    
    def str_to_lines(self, text, **kwargs):
        if text == None:
            return None
    
        args = tls.get_kwargs({
            'empty': self.empty_text,
            'replace': self.empty_lines,
            'size': self.size
        }, **kwargs)
        
        l = rgx.extract_numbers_and_chars(text, args['empty'])
        l = ds.remove_all(l, 0)
        
        if self.size == None:
            args['size'] = self.guess_size(l)
        if args['size'] == None:
            error_msg = 'Cannot extract a square from the text input given'
            raise ValueError(error_msg)
                
        ds.replace_in_nested_lists(l, args['empty'], args['replace'])
        chunked = ds.chunk_list(l, args['size'] * args['size'])
        return chunked



# =============================================================================
# Generate Grid
# =============================================================================


class CheckGrid:
    def __init__(self):
        pass
    
    @staticmethod
    def run(lines):
        print(lines)
        lines = ds.apply_funcs_to_lists(lines, [clrs.rm_clr, int], [None])
        # print(lines)
        # time.sleep(10)
        for i, l in enumerate(lines):
            if ds.has_duplicates(l, [None]):
                # print(i, l, '\nligne FALSE')
                return False
            # else:
            #     print(l)
            
        for y in range(9):
            col = [lines[x][y] for x in range(9)]
            if ds.has_duplicates(col, [None]):
                # print(i, col, '\ncol FALSE')
                return False

        for i in range(9):
            square = [lines[i - i % 3 + x][(i * 3) % 9 + y] for y in range(3) for x in range(3)]
            if ds.has_duplicates(square, [None]):
                # print(i, col, '\nsquare FALSE')
                return False


class CreaGrid:
    def __init__(self, size=3, difficulty=1, empty_lines='0', uniqueness=True):
        self._size = None
        self._length = None
        self.difficulty = difficulty
        self.empty_lines = empty_lines
        self.uniqueness = uniqueness
        
        self.grid = Grid()
        self.max_size = 5
        self.size = size

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int) or not 2 < new_size <= self.max_size:
            error_msg = f'Size must be int between 2 and {self.max_size}'
            raise ValueError(error_msg)
        self._size = new_size
        self._length = self.size * self.size

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, new_length):
        max_ = self.max_size * self.max_size
        sqrt = cal.perfect_sqrt(new_length)
        if (not isinstance(new_length, int)
            or not 4 <= new_length <= max_ or sqrt == None):
            error_msg = (
                f'Length must be an int between 4 and {max_} '
                f'and a perfect square'
            )
            raise ValueError(error_msg)
        self._length = new_length
        self._size = sqrt

    def rand(self, size=None):
        size = tls.if_none(size, self.size)
        length = size * size
        
        lines = []
        for i in range(length):
            row = []
            for i in range(length):
                n = random.randint(0, length)
                row.append(n)
            lines.append(row)
        print(lines)
        self.grid.lines = lines 
        return self.grid

    def status(self, text_clr=Color.BRIGHT_BLUE):
        status = (
            f"{clr('Size: ', text_clr):<30}{str(self.size)}\n"
            f"{clr('Max size: ', text_clr):<30}{str(self.max_size)}\n"
            f"{clr('Length: ', text_clr):<30}{str(self.length)}\n"
            f"{clr('Difficulty: ', text_clr):<30}{str(self.difficulty)}\n"
            f"{clr('Empty_lines: ', text_clr):<30}{str(self.empty_lines)}\n"
            f"{clr('Uniqueness: ', text_clr):<30}{str(self.uniqueness)}\n"
        )
        return status
    
    def show_status(self, text_clr=Color.BRIGHT_BLUE):
        print(self.status(text_clr))


# =============================================================================
# Sudoku
# =============================================================================


class Sdk:
    def __init__(self, grid, style):
        self._grid = None
        self.set_grid(grid)
        self._style = None
        self.set_style(style)
        
    @property
    def style(self):
        return self._style
    
    @property
    def grid(self):
        return self._grid
    
    @style.setter
    def style(self, new_style):
        self._size = self.set_style(new_style)
    
    def set_style(self, style):
        if not isinstance(style, Style):
            error_msg = (
                f"{self.__class__.__name__}.{self.set_style.__name__} "
                f"expects an instance of Style, "
                f"got {type(style).__name__} instead."
            )
            raise TypeError(error_msg)
        self._style = style
    
    def set_grid(self, grid):
        if not isinstance(grid, Grid):
            error_msg = (
                f"{self.__class__.__name__}.{self.set_grid.__name__} "
                f"expects an instance of Grid, "
                f"got {type(grid).__name__} instead."
            )
            raise TypeError(error_msg)
        self._grid = grid
    
    def show_as_list(self):
        print(self.grid)
    
    def show_simple(self, empty=' '):
        grid = Grid(ds.replace_in_nested_lists_cp(self.grid.lines, self.grid.empty_lines, empty), empty_lines=' ')
        for i, l in enumerate(grid.lines):
            print(*l, sep=' | ')
            if i != grid.length - 1:
                print(self.sep())
            
    def sep(self, sep='-', n=None):
        n = tls.if_none(n, self.grid.length * 4 - 3)
        return sep * n

    def init_show(self):
        vals = self.style.properties
        # print(vals)
        cp = ['' for _ in range(11)]
        off = 0
        for i, l in enumerate(self.grid.lines):
            if i == 3 or i == 6:
                for j in range(19): 
                    cp[i + off] += vals['sep_horz']
                    if j == 5 or j == 12:
                        cp[i + off] += vals['sep_cross']
                off += 1
            for x, n in enumerate(l):
                if n == None:
                    value = clr(' ', clrs.get_256_bg_clr_code(95))
                else:
                    value = str(n)
                space = ' ' if x < len(l) - 1 else ''
                # space = ' '
                cp[i + off] += clr(value + space, vals['digit'])
                if x == 2 or x == 5:
                    cp[i + off] += vals['sep_vert'] + clr(' ', vals['digit'])
        return cp
    
    def show(self):
            s = self.init_show()
            vals = self.style.properties
            
            print('\n' * vals['margin_top'], end='')
            for l in s:
                print(vals['indent'] * ' ', l, sep='')
            print('\n' * vals['margin_bot'], end='')



# =============================================================================
# Sudoko Handler
# =============================================================================

class SdkHandler:
    def __init__(self, sdk=None):
        self._sdk = None 
        
        self.set_sdk(sdk)
        
    @property
    def sdk(self):
        return self._sdk
    
    @sdk.setter
    def sdk(self, new_sdk):
        print('setter')
        self.set_sdk(new_sdk)
        
    def set_sdk(self, new_sdk):
        if new_sdk != None and not isinstance(new_sdk, Sdk):
            error_msg = (
                f"{self.__class__.__name__}.{self.set_sdk.__name__} "
                f"expects an instance of Sdk, "
                f"got {type(new_sdk).__name__} instead."
            )
            raise TypeError(error_msg)
        self._sdk = new_sdk
        
    def solve(self):
        if self.sdk == None:
            error_msg = (
                f"unsupported use of `{self.solve.__name__}` method "
                f"for: 'NoneType'"
            )
            raise TypeError(error_msg)
        print('\nsolving\n')
        self.solve_sdk()
        
    def is_valid_sdk(self, sdk):
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
    
    def modif_sdk(self, sdk, coord, new_value):
        new_value = None if new_value == None else clr(str(new_value), clrs.get_256_bg_clr_code(219) + Color.BLACK + Color.BOLD)
        sdk[coord[1]][coord[0]] = new_value

    def increment_2d(self, coord, inc, size_x, size_y):
        x = (coord[0] + inc) % size_x
        y = coord[1] + (coord[0] + inc) // size_x
        if x > size_x - 1 or y > size_y - 1:
            return False
        return (x, y)            
    
    def solve_sdk(self):
        sdk = self.sdk.grid.lines
        coord = (0, 0)
        coord = ds.find_from_in_2d_list(sdk, None, coord)
        if coord == False:
            print("\n" + clr('-------SUCCESS------', Color.BRIGHT_GREEN) + "\n")
            return True
        
        for i in range(9):
            self.modif_sdk(sdk, coord, i + 1)
            
            tls.clear_screen()
            
            self.sdk.show()
            ret = self.is_valid_sdk(sdk)
            time.sleep(0.05)
            

            if ret == True:
                if self.solve_sdk() == True:
                    return True
                
        self.modif_sdk(sdk, coord, None)
        return False
