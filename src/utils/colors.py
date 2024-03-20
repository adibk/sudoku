##################################################################################################################################
# Terminal Colors
##################################################################################################################################

class Color:
    # ANSI escape sequences for text colors
    END = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'  # Grey
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # ANSI escape sequences for text styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    STRIKETHROUGH = '\033[9m'
    
    # Standard Background Colors
    BLACK_BG = '\033[40m'
    RED_BG = '\033[41m'
    GREEN_BG = '\033[42m'
    YELLOW_BG = '\033[43m'
    BLUE_BG = '\033[44m'
    MAGENTA_BG = '\033[45m'
    CYAN_BG = '\033[46m'
    WHITE_BG = '\033[47m'

    # Bright Background Colors
    BRIGHT_BLACK_BG = '\033[100m'
    BRIGHT_RED_BG = '\033[101m'
    BRIGHT_GREEN_BG = '\033[102m'
    BRIGHT_YELLOW_BG = '\033[103m'
    BRIGHT_BLUE_BG = '\033[104m'
    BRIGHT_MAGENTA_BG = '\033[105m'
    BRIGHT_CYAN_BG = '\033[106m'
    BRIGHT_WHITE_BG = '\033[107m'

def list_basic_16_clrs():
    # Foreground colors
    for i in range(30, 38):
        print(f"\033[{i}mForeground Color {i}\033[0m")

    # Background colors
    for i in range(40, 48):
        print(f"\033[{i}mBackground Color {i}\033[0m")

    # Bright versions
    for i in range(90, 98):
        print(f"\033[{i}mBright Foreground Color {i}\033[0m")
    for i in range(100, 108):
        print(f"\033[{i}mBright Background Color {i}\033[0m")

def list_256_clrs():
    # Foreground colors
    for i in range(0, 256):
        print(f"\033[38;5;{i}mColor {i}\033[0m", end=' ')
        if i % 10 == 0:
            print()  # Newline every 10 colors

    # Background colors
    for i in range(0, 256):
        print(f"\033[48;5;{i}m Color {i} \033[0m", end=' ')
        if i % 10 == 0:
            print()  # Newline every 10 colors

def test_true_color():
    for r in range(0, 256, 51):  # Increment by 51 for a simple gradient
        for g in range(0, 256, 51):
            for b in range(0, 256, 51):
                print(f"\033[38;2;{r};{g};{b}m True Color: R{r} G{g} B{b} \033[0m", end=' ')
            print()

def get_256_clr_code(n):
    """
    Returns the ANSI escape code for the n-th color in the 256-color palette.
    
    :param n: The color number (0-255).
    :return: The ANSI escape code for the foreground color.
    """
    if 0 <= n <= 255:
        return f"\033[38;5;{n}m"
    return None

def get_256_bg_clr_code(n):
    """
    Returns the ANSI escape code for the n-th background color in the 256-color palette.
    
    :param n: The background color number (0-255).
    :return: The ANSI escape code for the background color.
    """
    if 0 <= n <= 255:
        return f"\033[48;5;{n}m"
    return None

def str_clr(s, clr=None):
    clr = clr if clr != None else Color.BRIGHT_RED 
    return clr + s + Color.END

def clr(lst, clr=Color.BRIGHT_RED):
    clr_lst = []
    if not isinstance(clr, list):
        clr = [clr]
    i = 0
    if isinstance(lst, list):
        for str in lst:
            clr_lst.append(clr[i % len(clr)] + str + Color.END)
            i += 1
        return clr_lst
    return str_clr(lst, clr[0])

def put(str, clr=None):
    print(str_clr(str, clr))

def clr_dict(dict_, new_clr):
    new_dict = {key: clr(value, new_clr) for key, value in dict_.items()}
    return new_dict
