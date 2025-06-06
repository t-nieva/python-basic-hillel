test_list_1 = [0, 1, 7, 2, 4, 8]
test_list_2 = [1, 3, 5]
test_list_3 = [6]
test_list_4 = []


def sum_of_el_with_even_indexes(my_list):
    if not my_list:
        print(0)
    else:
        print(sum(my_list[::2]) * my_list[-1])


sum_of_el_with_even_indexes(test_list_1)
sum_of_el_with_even_indexes(test_list_2)
sum_of_el_with_even_indexes(test_list_3)
sum_of_el_with_even_indexes(test_list_4)
