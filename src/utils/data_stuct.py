# =============================================================================
# Mix Data structure
# =============================================================================



# =============================================================================
# Lists
# =============================================================================


def chunk_list(list_, chunk_size):
    """
    Splits the input list into smaller lists (chunks) of a specified size.
    
    :param list_: The list to be chunked.
    :param chunk_size: The size of each chunk.
    :return: A list of lists, where each inner list is a chunk of the original list.
    """
    return [list_[i:i + chunk_size] for i in range(0, len(list_), chunk_size)]

def replace_in_nested_lists(list_, old, new_):
    """
    Recursively replace elements in all nested lists.

    :param list_: The nested list to process.
    :param old: The value to be replaced.
    :param new_: The value to replace with.
    """
    for i in range(len(list_)):
        if list_[i] == old:
            list_[i] = new_
        elif isinstance(list_[i], list):
            replace_in_nested_lists(list_[i], old, new_)
            
def replace_in_nested_lists_cp(list_, old, new_):
    """
    Recursively replace elements in all nested lists
    in `cp` which is a `list_` copy.
    
    :param list_: The nested list to process.
    :param old: The value to be replaced.
    :param new_: The value to replace with.
    :return: `cp`, modified copy of `list_` 
    """
    cp = list_
    for i in range(len(cp)):
        if cp[i] == old:
            cp[i] = new_
        elif isinstance(cp[i], list):
            replace_in_nested_lists(cp[i], old, new_)
    return cp

def has_duplicates(list_, exclude=None):
    """
    Check if the given list contains any duplicate elements, ignoring specified values.

    :param list_: List to check for duplicates.
    :param exclude: A list of values to ignore when checking for duplicates. Defaults to None.
    :return: True if duplicates exist (excluding ignored values), False otherwise.
    """
    if exclude is None:
        exclude = []

    filtered_list = [item for item in list_ if item not in exclude]
    return len(filtered_list) != len(set(filtered_list))

def find_from(list_, elem, start=0, end=None):
    """
    Searches for an element in a list starting from a specified index and up to an optional end index.

    :param list_: The list to search.
    :param elem: The element to search for.
    :param start: The index to start the search from. Defaults to 0.
    :param end: The index to end the search at. Defaults to None (search till the end of the list).
    :return: The index of the element if found within the specified range, or False if not found.
    """
    slice_end = end if end is not None else len(list_)
    slice_lst = list_[start:slice_end]
    
    try:
        relative_index = slice_lst.index(elem)
        return start + relative_index
    except ValueError:
        return False
    
def find_from_in_2d_list(lst_of_lsts, elem, start=(0, 0), end=None):
    """
    Searches for an element in a 2D list (list of lists) within the specified range and returns its coordinates
    (x, y) if found. The search range is defined by start and end coordinates.

    :param lst_of_lsts: The 2D list to search.
    :param elem: The element to search for.
    :param start: A tuple (x, y) representing the starting coordinates for the search.
    :param end: A tuple (x, y) representing the ending coordinates for the search. If None, searches until the end.
    :return: A tuple (x, y) representing the coordinates of the element if found, or False if not found.
    """
    start_x, start_y = start
    end_x, end_y = end if end is not None else (len(lst_of_lsts[0]), len(lst_of_lsts))
    
    for y in range(start_y, end_y):
        sublist = lst_of_lsts[y]
        # Determine the start and end indices for searching in the current row
        row_start = start_x if y == start_y else 0
        row_end = end_x if y == end_y - 1 else len(sublist)
        
        # Search within the specified range in the current row
        for x in range(row_start, row_end):
            if sublist[x] == elem:
                return (x, y)
    
    return False

def apply_funcs_to_lists(nested_list, funcs, exclude_values=None):
    """
    Applies multiple functions to every element in a nested list, excluding specified values.

    :param nested_list: The nested list to process.
    :param funcs: A list of functions to apply to each element.
    :param exclude_values: A list of values to exclude from processing.
    :return: A new nested list with the functions applied to each element, excluding the specified values.
    """
    if exclude_values is None:
        exclude_values = []

    if not isinstance(funcs, list):
        funcs = [funcs]

    result = []
    for item in nested_list:
        if isinstance(item, list):
            # Recursively apply the functions to sublists
            result.append(apply_funcs_to_lists(item, funcs, exclude_values))
        elif item not in exclude_values:
            # Apply each function in sequence if the item is not in the list of values to exclude
            for func in funcs:
                item = func(item)
            result.append(item)
        else:
            # Directly append the item if it is in the list of values to exclude
            result.append(item)
    return result



# =============================================================================
# Dictionary
# =============================================================================


def all_keys_present(source_dict, target_dict):
    '''
    Check if all keys from the source dictionary are present in the target dictionary.

    :param source_dict: The dictionary whose keys need to be checked.
    :param target_dict: The dictionary in which to look for the keys.
    :return: True if all keys from `source_dict` are in `target_dict`, False otherwise.
    :rtype: bool

    :Example:
    >>> source = {'a': 1, 'b': 2}
    >>> target = {'a': 3, 'b': 4, 'c': 5}
    >>> all_keys_present(source, target)
    True
    '''
    return all(key in target_dict for key in source_dict)

def keys_not_in_target(source_dict, target_dict):
    '''
    :return: the keys in the source dictionary `source_dict` that are not
    in the targe dictionary `target_dict`
    '''
    return set(source_dict.keys()) - set(target_dict.keys())
