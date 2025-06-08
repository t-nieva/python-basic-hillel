test_list_1 = [0, 1, 0, 12, 3]
test_list_2 = [0]
test_list_3 = [1, 0, 13, 0, 0, 0, 5]
test_list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


def test(test_list):
    insert_position = 0
    for i, el in enumerate(test_list):
        if el != 0:
            test_list[insert_position] = el
            insert_position += 1

    for i in range(insert_position, len(test_list)):
        test_list[i] = 0
    print(test_list)


test(test_list_1)
test(test_list_2)
test(test_list_3)
test(test_list_4)
