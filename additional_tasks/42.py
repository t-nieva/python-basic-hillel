# Дана послідовність слів. Написати функцію, яка повертає послідовність
# слів, в якій у словах довжини 3 всі літери великі, а всі слова, що
# починаються на "q" або "f" виключені. Використовувати ланцюжки.
# Приклад: ["The", "quick", "brown", "fox"] -> ["THE", "brown"]


def modified_sequence(input_sequence):
    filtered = list(
        filter(lambda word: not word.lower().startswith(("q", "f")), input_sequence)
    )
    return list(map(lambda word: word.upper() if len(word) == 3 else word, filtered))


print(modified_sequence(["The", "quick", "brown", "fox"]))


# Solution
# def funk2(words_list):
#     return map(
#         lambda x: x.upper() if len(x) == 3 else x,
#         filter(lambda x: not x.startswith(('q', 'f')), words_list)
#     )
#
#
# words = ["The", "quick", "brown", "fox"]
#
# print(list(funk2(words)))
