
# =============================================================================
# Tools
# =============================================================================

import sys
from bs4 import BeautifulSoup

def N():
    print()

def safe_max(l, default=None):
    if not l:
        return default
    return max(l)

def max_len(l):
    return safe_max([len(i) for i in l], 0)

def max_lists(*lists):
    ret = 0
    for l in lists:
        ret = max(ret, max_len(l))
    return ret

def if_none(val, new_val):
    return val if val != None else new_val

def sort_tuple(tup):
    return tuple(sorted(tup))

def pretty_tuple(tup):
    output = ', '.join(str(item) for item in tup)
    return output

def clean_str(str):
    return str.replace('\t', '').replace('\n', '').replace('\r', '')

def strip_tags(html_str):
    # Use BeautifulSoup to parse and extract text without tags
    soup = BeautifulSoup(html_str, 'html.parser')
    return soup.get_text()

def get_kwargs(defaults, **kwargs):
    '''
    :return: go through defaults values and return a dict. with the
    `key: value` from `kwargs` if `key` found in `kwargs`, otherwise
    `key: value` from `defaults`
    
    Example:
    >>> get_kwargs({'a': 3, 'c': 2}, **{'a': 0, 'd': 8}))
    {'a': 0, 'c': 2}
    '''
    ret = {}
    for key, value in defaults.items():
        ret[key] = value if key not in kwargs else kwargs[key]
    return ret

def clear_screen():
     # Clear the screen
    sys.stdout.write("\033[2J\033[H")  # ANSI escape code to clear the screen and move cursor to top-left
    sys.stdout.flush()
