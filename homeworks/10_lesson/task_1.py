from inspect import isgenerator


def pow(x: int | float) -> int | float:
    """
    Calculates the square of a number.
    """
    return x**2


def some_gen(begin, end, func):
    """
    begin: the first element of the sequence
    end: the number of elements in the sequence
    func: a function that generates the next value in the sequence
    """
    value = begin
    for _ in range(end):
        yield value
        value = func(value)


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, "Test1"
assert list(gen) == [2, 4, 16, 256], "Test2"
print("OK")
