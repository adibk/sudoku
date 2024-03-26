import json

from utils import colors as clrs
from utils.colors import Color

from utils import data_stuct as ds
from utils import tools as tls


styles = {
    'default': {
        'margin': 0,
        'indent': 0,
        'margin_bot': 3,
        'margin_right': 3,
        'margin_left': 3,
        'margin_top': 3,
        'corner': '/',
        'frame': '.',
        'frame_vert': ':',
        'frame_horz': ':',
        'frame_bot': '-',
        'frame_top': ':',
        'frame_right': ':',
        'frame_left': ':',
        'frame_clr': Color.BLUE,
        'sep_vert': '|',
        'sep_horz': '-',
        'sep_cross': '+',
        'sep_clr': Color.RED,
        'digit': Color.BRIGHT_CYAN,
        'no_digit': '.',
        'no_digit_clr': Color.BRIGHT_CYAN_BG,
    },
      
    'simple_margin': {
        'indent': 5,
        'top_margin': 3,
        'bot_margin': 3,
    },
    
    'wood': {
        'indent': 5,
        'top_margin': 3,
        'bot_margin': 3,
        'vert': '|',
        'horz': '=',
        'cross': 'x',
        'sep_clr': clrs.get_256_clr_code(167),
        'clr': clrs.get_256_bg_clr_code(95) + clrs.get_256_clr_code(230)
    },
    
    'ocean': {
        'indent': 5,
        'top_margin': 3,
        'bot_margin': 3,
        'vert': '|',
        'horz': '~',
        'cross': '+',
        'sep_clr': clrs.get_256_clr_code(75) + Color.BOLD,
        'clr': clrs.get_256_bg_clr_code(123) + clrs.get_256_clr_code(235) + Color.ITALIC
    },
    
    'my_style': {
        'indent': 10,
        'margin_bot': 3,
        'margin_right': 3,
        'margin_left': 3,
        'margin_top': 3,
        'corner': '/',
        'frame': '.',
        'frame_vert': ':',
        'frame_horz': ':',
        'frame_bot': '-',
        'frame_top': ':',
        'frame_right': ':',
        'frame_left': ':',
        'frame_clr': Color.BLUE,
        'sep_vert': '|',
        'sep_horz': '-',
        'sep_cross': '+',
        'sep_clr': Color.RED,
        'digit': Color.BRIGHT_CYAN,
        'no_digit': '.',
        'no_digit_clr': Color.BRIGHT_CYAN_BG,
    }
}


class Style:
    def __init__(self, **kwargs):
        self._default = styles['default']
        self._properties = None
    
        self.set_properties(**kwargs)
    
    @property
    def default(self):
        return self._default
    
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, values):
        self.set_properties(**values)
    
    def validate_kwargs(self, kwargs):
        diff = ds.keys_not_in_target(kwargs, self.default)
        if  diff != set():
            raise ValueError(
                f"Invalid keyword argument: {', '.join(list(diff))}")

    def set_properties(self, **kwargs):
        self.validate_kwargs(kwargs)
        self._properties = tls.get_kwargs(self.default, **kwargs)

    def show(self, **kwargs):
        to_show = (self.default if kwargs.get('default') == True 
                   else self.properties)
        indent = kwargs.get('indent') if kwargs.get('indent') != None else 4
        print(json.dumps(to_show, indent=indent))


import sys
import tty
import termios
import curses

class CreateStyle:
    def __init__(self):
        pass
        
    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
    def run(self):
        print("Press any key ('q' to exit):")
        while True:
            key = self.getch()
            print(f"You pressed: {key}")

            if key == 'q':
                print("Exiting...")
                break
            
    def get_style(self):
        return Style(**styles['my_style'])

# my_style = Style(**styles['my_style'])
# my_style.show()
# my_style.properties = {'margin':800}
# my_style.show()

