# Дана послідовність слів. Написати функцію, яка повертає послідовність
# слів з вихідної послідовності відсортованих по алфавіту, довжина
# яких більше трьох букв і до кожного слова застосовано метод title().
#
# Приклад: ["HellO", "WORLD", "names", "Is", "Sam", "NO", "apple"]
# Результат: ['Apple', 'Hello', 'Names', 'World']


def sorted_list(words_list):
    res = [word.lower().title() for word in words_list if len(word) > 3]
    res.sort()
    return res


test_list = ["HellO", "WORLD", "names", "Is", "Sam", "NO", "apple"]
print(sorted_list(test_list))


# Solution 2
def func(list_str):
    return sorted(filter(lambda x: len(x) > 3, map(str.title, list_str)))


strings = ["HellO", "WORLD", "names", "Is", "Sam", "NO", "apple"]
print(func(strings))
