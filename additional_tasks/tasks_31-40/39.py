from typing import List

# Напишіть функцію find_longest_word, яка прийматиме список слів і
# повертати найдовше слово зі списку.
# Анотуйте типи аргументів і значення функції, що повертається.
#
# Приклад виклику функції та очікуваного виводу:
words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(words)
# print(result)
# Очікуваний висновок: "dragonfruit"


def find_longest_word(words_list: List[str]) -> str:
    return max(words_list, key=len)


print(find_longest_word(words))
