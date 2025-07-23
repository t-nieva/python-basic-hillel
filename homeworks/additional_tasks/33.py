# Напишіть функцію is_subset, яка приймає дві множини set1 і set2 і
# перевіряє, чи є set1 підмножиною set2. Функція має повертати
# True, якщо всі елементи set1 містяться в set2, і False в іншому
# Випадок. Функція має бути реалізована без використання вбудованих методів
# issubset або <=.
#
# Приклад множин
my_set_1 = {1, 2, 3}
my_set_2 = {1, 2, 3, 4, 5}
#
# Приклад висновку:
# True


def is_subset(set1, set2):
    for item in set1:
        if item not in set2:
            return False
    return True


print(is_subset(my_set_1, my_set_2))
