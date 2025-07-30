# Напишіть функцію, яка приймає на вхід список функцій та значення, а потім
# застосовує композицію цих функцій значення, повертаючи кінцевий результат.
#
# Приклад:
# add_one = lambda x: x + 1
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
#
# functions = [add_one, double, subtract_three]
# compose_functions(functions, 5) має вивести 9


def compose_functions(functions_list, value):
    for function in functions_list:
        value = function(value)
    return value


# add_one = lambda x: x + 1
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
# functions = [add_one, double, subtract_three]
functions = [lambda x: x + 1, lambda x: x * 2, lambda x: x - 3]
print(compose_functions(functions, 5))


# Solution
# def compose_functions(s, k):
#     result = k
#     for i in s:
#         result = i(result)
#     return result
#
#
# add_one = lambda x: x + 1
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
# functions = [add_one, double, subtract_three]
# print(compose_functions(functions, 5))
