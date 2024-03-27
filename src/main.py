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



# =============================================================================
# Main
# =============================================================================


def init_main():
    pass

def exit_main():
    pass


def main():
    
    init_main()
        
    crea = CreaGrid()
    crea.rand()
    crea.length = 16
    crea.show_status()

    return    
    text = SdkExples_2.solve['9x9_0_almost_empty'][0]
    grid = Grid(text, empty_lines=None)

    crea = module_style.CreateStyle()
        
    sdk = Sdk(grid, crea.get_style())
    # sdk.show_simple()
    # sdk.show()
    
    sdk_handler = SdkHandler()
    sdk_handler.sdk = sdk
    sdk_handler.sdk.grid.show_status()
    sdk_handler.solve(0.0001)

    exit_main()
    return
    
if __name__ == "__main__":
    main()

