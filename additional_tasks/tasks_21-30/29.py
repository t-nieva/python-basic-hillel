# Даний список цілих чисел довжини 1 і більше. Написати функцію, яка повертає список
# довжини 2, що складається з першого та останнього елемента вхідного списку.
# [1, 2, 3] -> [1, 3], [7, 4, 6, 2] -> [7, 2], [5] -> [5, 5]

list_1 = [1, 2, 3]
list_2 = [7, 4, 6, 2]
list_3 = [5]


def new_list(my_list):
    if not my_list:
        return "Invalid input data"
    return [my_list[0], my_list[-1]]


print(new_list(list_1))
print(new_list(list_2))
print(new_list(list_3))
