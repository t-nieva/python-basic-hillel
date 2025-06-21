def second_index(text, some_str):
    first = text.find(some_str)
    if first == -1:
        return None
    second = text.find(some_str, first + len(some_str))
    if second == -1:
        return None
    return second


assert second_index("sims", "s") == 3, "Test1"
assert second_index("find the river", "e") == 12, "Test2"
assert second_index("hi", "h") is None, "Test3"
assert second_index("Hello, hello", "lo") == 10, "Test4"
assert second_index("Hellllo", "ll") == 4, "Test5"
assert second_index("Helllo", "ll") is None, "Test6"
print("ОК")
