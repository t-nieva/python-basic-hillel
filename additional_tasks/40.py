from functools import reduce

# Напишіть функцію, яка приймає на вхід список чисел та повертає суму
# квадратів тільки парних чисел зі списку, використовуючи функціональні
# підходи (наприклад, map, filter та reduce).
#
# Приклад:
# Введіть числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72


def sum_of_squares_even_numbers(num_list):
    filtered = filter(lambda item: item % 2 == 0, num_list)
    return reduce(lambda x, y: x + y, map(lambda item: item**2, filtered))


print(sum_of_squares_even_numbers([4, 6, 3, 4, 2, 3, 9, 0, 7]))
