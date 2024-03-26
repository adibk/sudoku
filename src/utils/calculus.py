def perfect_sqrt(nb):
    """
    Calculate the square root of a nb if it's a perfect square.
    A perfect square is an integer that is the square of an integer.
    For example, 16 is a perfect square because 4 * 4 = 16.
    This function returns the integer square root if the nb is a perfect
    square. Otherwise, it returns None.
    
    Args:
    - nb (int): The nb for which to find the square root.
    
    Returns:
    - int or None: The square root of the nb if it's a perfect square,
    otherwise None.
    """
    if nb < 0:
        return None
    if nb == 0 or nb == 1:
        return nb
    left, right = 1, nb // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == nb:
            return mid
        elif square < nb:
            left = mid + 1
        else:
            right = mid - 1

    return None

def is_perfect_sqrt(nb):
    return perfect_sqrt(nb) != None
