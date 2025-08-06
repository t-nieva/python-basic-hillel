# Даний список, що складається з даних різного типу.
# Повернути новий список, де за допомогою функції map() кожен елемент типу
# int початкового списку приведений до типу str, елементи решти всіх типів
# передаються в новий список без зміни їх типу.
# У якості вхідної функції в map використовувати lambda-функцію.

values = [1, 2, "3", "forth", "end", 99, True, None]


def get_new_list(my_list):
    return list(map(lambda n: str(n) if type(n) is int else n, my_list))


print(get_new_list(values))
