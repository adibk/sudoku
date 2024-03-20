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
