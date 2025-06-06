test_list_1 = [0, 1, 0, 12, 3]
test_list_2 = [0]
test_list_3 = [1, 0, 13, 0, 0, 0, 5]
test_list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


def test(test_list):
    i = 0
    n = len(test_list)
    for _ in range(n):
        if test_list[i] == 0:
            test_list.pop(i)
            test_list.append(0)
        else:
            i += 1
    print(test_list)


test(test_list_1)
test(test_list_2)
test(test_list_3)
test(test_list_4)
