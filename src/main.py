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

from examples.expls import SdkExples
from examples.expls import SdkExples_2

from sdk import sdk
from sdk.sdk import Sdk
from sdk.sdk import Grid
from sdk.sdk import CreaGrid
from sdk.sdk import CheckGrid
from sdk.sdk import SdkHandler
from sdk import style as module_style
from sdk.style import Style

def print_ascii():
    for i in range(32, 127):
        print(chr(i), end=' ')
    print()

    for i in range(128, 256):
        print(chr(i), end=' ')
    print()

    for i in range(1024):
        try:
            print(chr(i), end=' ')
        except UnicodeEncodeError:
            pass
    print()
    


def print_unicode_characters_columns(start=32, end=1000, column_count=5):
    for i in range(start, end):
        try:
            end_char = '\n' if (i - start) % column_count == column_count - 1 else '\t'
            print(f"{chr(i)}: {i}", end=end_char)
        except UnicodeEncodeError:
            pass
    print()

# print_unicode_characters_columns(32, 1400)

# =============================================================================
# Main
# =============================================================================


def init_main():
    pass

def exit_main():
    pass


def main():
    
    init_main()
         
         
    
    # grid = Grid()
    # grid.text = SdkExples_2.text['2x2_0'][0]
    # grid.empty_lines = '0'
    # grid.show_status()
    
    # return

    crea = CreaGrid(size=3)
    # crea.length = 9
    crea.empty()
    
    # return
    crea.show_status()

    # return 
    crea_style = module_style.CreateStyle('wood')
    
    # return
    
    sdk = Sdk(crea.grid, crea_style.get_style())
    
    sdk_handler = SdkHandler(sdk)
    
    sdk_handler.sdk.grid.show_status()
    # return
    sdk_handler.solve(100)

    sdk.grid.show_status()
    # sdk_handler.sdk.grid.show_status()
    
    return    
    
    # text = SdkExples_2.solve['9x9_0_almost_empty'][0]
    # grid = Grid(text, empty_lines=0)

    # crea = module_style.CreateStyle('my_style')
        
    # sdk = Sdk(grid, crea.get_style())
    # # sdk.show_simple()
    # # sdk.show()
    
    # sdk_handler = SdkHandler()
    # sdk_handler.sdk = sdk
    # sdk_handler.sdk.grid.show_status()
    # sdk_handler.solve(0.0001, )

    exit_main()
    return
    
if __name__ == "__main__":
    main()

