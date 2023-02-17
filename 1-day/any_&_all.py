def check_any_all():
    """
    any() returns True if ang of the sequence value is True
    """
    list_of_bool = [True, True, True,1]
    print(any(list_of_bool))  # True
    print(all(list_of_bool))  # False

if __name__ == '__main__':
    check_any_all()