def split_list(my_list):
    res = []
    if len(my_list) % 2 == 0:
        middle = int(len(my_list) / 2)
    else:
        num, remainder = divmod(len(my_list), 2)
        middle = num + remainder
    list_1 = my_list[:middle]
    list_2 = my_list[middle:]
    res.append(list_1)
    res.append(list_2)
    print(res)


test_1 = [1, 2, 3, 4, 5, 6]  # => [[1, 2, 3], [4, 5, 6]]
test_2 = [1, 2, 3]  # => [[1, 2], [3]]
test_3 = [1, 2, 3, 4, 5]  # => [[1, 2, 3], [4, 5]]
test_4 = [1]  # => [[1], []]
test_5 = []  # => [[], []]

split_list(test_1)
split_list(test_2)
split_list(test_3)
split_list(test_4)
split_list(test_5)
