import re

def extract_nbs(text):
    """
    Extracts all numbers from the given text and returns them as a list.
    
    :param text: A string containing numbers.
    :return: A list of numbers (as strings) found in the text.
    """
    nb_pattern = r"-?\d+\.?\d*"
    nbs = re.findall(nb_pattern, text)
    converted_nbs = []
    for nb in nbs:
        try:
            # Convert to int if possible
            converted_nb = int(nb)
        except ValueError:
            # Convert to float if int conversion fails
            converted_nb = float(nb)
        converted_nbs.append(converted_nb)
    
    return converted_nbs

def extract_nbs_as_positive(text):
    """
    Extracts all sequences of digits from the given text and returns them as positive integers,
    regardless of their original format (negative or embedded in text).
    
    :param text: A string containing numbers.
    :return: A list of positive integers found in the text.
    """
    nb_pattern = r"\d+"
    nbs = re.findall(nb_pattern, text)
    positive_ints = [int(nb) for nb in nbs]
    
    return positive_ints

def extract_numbers_and_chars(text, *chars):
    """
    Extracts all numbers as positive integers and specific characters from a given text.
    
    :param text: The input string to extract from.
    :param chars: Variable length argument list of characters to extract from the text.
    :return: A list of positive integers and specified characters found in the text.
    """
    pattern = r"\d+|" + "|".join(re.escape(char) for char in chars)
    matches = re.findall(pattern, text)
    extracted = [int(match) if match.isdigit() else match for match in matches if match.isdigit() or match in chars]
    
    new_lst = []
    for elem in extracted:
        if isinstance(elem, int) and str(elem) in chars:
            new_lst.append(str(elem))
        else:
            new_lst.append(elem)
    return new_lst

# import utils.data_stuct as ds
# test = "str 0 1 3 str  2 4 df 4 ccc 344 0 2 str stts 0"
# l = extract_numbers_and_chars(test, 'str', 't')
# l = ds.remove_all(l, [0, 3, 'str'])
# print(l)