from secrets import randbelow

def number_between(min: int, max: int) -> int:

    """
    Generate a random number between min and max.

    :param min: The minimum number to generate.
    :param max: The maximum number to generate.

    :return: A random number between min and max.
    """
    
    return randbelow(max - min) + min