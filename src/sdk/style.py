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
        'frame_horizon': ':',
        'frame_bot': '-',
        'frame_top': ':',
        'frame_right': ':',
        'frame_left': ':',
        'frame_clr': Color.BLUE,
        'sep_vert': '|',
        'sep_horizon': '-',
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
        'indent': 100,
        'margin_bot': 3,
        'margin_right': 3,
        'margin_left': 3,
        'margin_top': 3,
        'corner': '/',
        'frame': '.',
        'frame_vert': ':',
        'frame_horizon': ':',
        'frame_bot': '-',
        'frame_top': ':',
        'frame_right': ':',
        'frame_left': ':',
        'frame_clr': Color.BLUE,
        'sep_vert': '|',
        'sep_horizon': '-',
        'sep_cross': '+',
        'sep_clr': Color.RED,
        'digit': Color.BRIGHT_CYAN,
        'no_digit': '.',
        'no_digit_clr': Color.BRIGHT_CYAN_BG,
    }
}


class Style:
    def __init__(self, **kwargs):
        self.default = styles['default']
        self._properties = self.set_properties(self.default, **kwargs)
    
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, values):
        self._properties = self.set_properties(self.properties, **values)
    
    def validate_kwargs(self, kwargs):
        diff = ds.keys_not_in_target(kwargs, self.default)
        if  diff != set():
            raise ValueError(
                f"Invalid keyword argument: {', '.join(list(diff))}")

    def set_properties(self, default, **kwargs):
        self.validate_kwargs(kwargs)
        return tls.get_kwargs(default, **kwargs)

    def show(self, **kwargs):
        to_show = (self.default if kwargs.get('default') == True 
                   else self.properties)
        indent = kwargs.get('indent') if kwargs.get('indent') != None else 4
        print(json.dumps(to_show, indent=indent))

# my_style = Style(**styles['my_style'])
# my_style.show()
# my_style.properties = {'margin':800}
# my_style.show()

