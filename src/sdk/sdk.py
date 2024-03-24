from utils import calculus
from utils import tools as tls
from utils import rgx
from utils import data_stuct as ds

import sdk.style as module_style
from sdk.style import Style
from examples import expls

class Grid():
    def __init__(self, str):
        self.str = str
        
    def str_to_grid(self, empty='.', replace=None, size=3):
        l = rgx.extract_numbers_and_chars(self.str, empty)
        ds.replace_in_nested_lists(l, empty, replace)
        chunked = ds.chunk_list(l, size * size)
        return chunked
    

class Sdk:
    def __init__(self, grid, style):
        self.grid = grid
        self._style = self.set_style(style)
        self._size = self.set_size()
        self._length = self.size * self.size

    @property
    def size(self):
        return self._size
    
    @property
    def style(self):
        return self._style
    
    @style.setter
    def style(self, new_style):
        self._size = self.set_style(new_style)
    
    @property
    def length(self):
        return self._length
    
    def set_size(self):
        return calculus.perfect_sqrt(len(self.grid))
    
    def set_style(self, style):
        if not isinstance(style, Style):
            raise TypeError("Expected an instance of Style")
        self._style = style
    
    def show_as_list(self):
        print(self.grid)
    
    def show_simple(self, empty='.'):
        grid = ds.replace_in_nested_lists_cp(self.grid, None, empty)
        for i, l in enumerate(grid):
            print(*l, sep=' | ')
            if i != len(grid) - 1:
                print(self.sep())
            
    def sep(self, sep='-', n=None):
        n = tls.if_none(n, self.length * 4 - 3)
        return sep * n

    def show(self):
        pass

