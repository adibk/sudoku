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

from sdk import sdk
from sdk.sdk import Sdk
from sdk.sdk import Grid
from sdk.sdk import SdkHandler
from sdk import style as module_style
from sdk.style import Style



# =============================================================================
# Main
# =============================================================================


def init_main():
    pass

def exit_main():
    pass


def main():
    
    init_main()
    
    text = SdkExples.text['sdk_3x3_char_dot'][0]
    grid = Grid(text)
    # print(grid.text, grid.lines, grid.size, grid.length)

    crea = module_style.CreateStyle()
        
    sdk = Sdk(grid, crea.get_style())
    sdk.show_simple()
    sdk.show()
    
    sdk_handler = SdkHandler()
    sdk_handler.sdk = sdk
    sdk_handler.solve()

    
    exit_main()
    return
    
if __name__ == "__main__":
    main()

