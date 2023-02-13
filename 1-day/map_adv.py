from time import perf_counter

list_of_numbers = list(range(1_000_000)) # list of numbers []

start = perf_counter()

def kvadrat(list_of_numbers: list) -> list:
    """ return list of numbers which are squared

    Args:
        list_of_numbers (list): _description_

    Returns:
        list: _description_
    """

    return [ i**2 for i in list_of_numbers ]


def kvadrat_map(list_of_numbers: list) -> list:
    """ return list of numbers which are squared

    Args:
        list_of_numbers (list): _description_

    Returns:
        list: _description_
    """

    return list(map(lambda x: x**2, list_of_numbers))

# sonlar = kvadrat(list_of_numbers) # 0.5989165529999809

# sonlar = kvadrat_map(list_of_numbers) # 0.5947941710001032

sonlar = list(map(lambda x: x**2, list_of_numbers)) #0.4948713459998544

end = perf_counter()

print(end - start)
