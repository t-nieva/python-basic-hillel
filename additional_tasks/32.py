# Напишіть програму, яка приймає список слів і повертає список, містить тільки
# анаграми. Анаграми - це слова, складені з тих самих букв, але у різному
# порядку. Створіть функцію anagrams, яка приймає список слів як аргумент
# та повертає список анаграм. Використовуйте безліч і сортування букв у слові
# для перевірки на анаграму. Виведіть результат на екран.
#
# Приклад переданого списку слів:
my_lst = ["cat", "dog", "tac", "god", "act"]
#
# Приклад висновку:
# Анаграми: ['dog', 'god'], ['cat', 'tac', 'act']


def anagrams(words_lst):
    anagram_dict = {}
    for word in words_lst:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)

    groups = [group for group in anagram_dict.values() if len(group) > 1]
    return ", ".join(str(group) for group in groups)


print("Анаграми:", anagrams(my_lst))
