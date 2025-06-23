'''
Author: Alexandr Iapara
Description: A module for padding strings with specified characters and directions.
'''

def pad_string(string, space_amount, space_character=" ", direction="left"):
    '''
    Pads a string with a specified character and direction.

    Args:
        string (str): The string to be padded.
        space_amount (int): Number of padding characters to add.
        space_character (str, optional): The character to use for padding. Defaults to a single space.
        direction (str, optional): Direction to pad ('left' or 'right'). Defaults to 'left'.

    Returns:
        str: The padded string.

    Example:
        pad_string("hello", 3, "*", "right") -> "hello***"
    '''
    if direction.lower() == "left":
        result = (space_character * space_amount) + string
        return result
    elif direction.lower() == "right":
        result = string + (space_character * space_amount)
        return result

def pad_left(string, space_amount):
    '''
    Pads a string on the left with spaces.

    Args:
        string (str): The string to be padded.
        space_amount (int): Number of spaces to add on the left.

    Returns:
        str: The left-padded string.

    Example:
        pad_left("hello", 3) -> "   hello"
    '''
    result = pad_string(string, space_amount, " ", "left")
    return result

def pad_right(string, space_amount):
    '''
    Pads a string on the right with spaces.

    Args:
        string (str): The string to be padded.
        space_amount (int): Number of spaces to add on the right.

    Returns:
        str: The right-padded string.

    Example:
        pad_right("hello", 3) -> "hello   "
    '''
    result = pad_string(string, space_amount, " ", "right")
    return result