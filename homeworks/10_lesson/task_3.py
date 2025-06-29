def is_even(digit: int) -> bool:
    """
    Check if a number is even.

    :param digit: The number to check.
    :return: True if the number is even, False otherwise.
    """
    if digit % 2 == 0:
        return True
    return False


assert is_even(2) == True, "Test1"
assert is_even(5) == False, "Test2"
assert is_even(0) == True, "Test3"
print("OK")
