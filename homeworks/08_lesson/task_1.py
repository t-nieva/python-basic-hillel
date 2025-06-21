def add_one(some_list):
    some_string = ""
    for num in some_list:
        some_string += str(num)
    some_num = int(some_string) + 1
    new_list = [int(el) for el in str(some_num)]
    return new_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("ОК")
