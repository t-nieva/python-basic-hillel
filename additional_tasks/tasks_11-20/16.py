# Напишіть програму, яка запитує у користувача рядок і виводить на екран
# кількість голосних і приголосних літер в ній. Використовуйте функцію len()
# для підрахунку кількості літер. Виведіть результат на екран за допомогою
# команди print. Розв'язати задачу для латиниці.
#
# Приклад:
# Введіть рядок: Hello World
# Кількість голосних літер: 3
# Кількість приголосних літер: 7
import string

text = input("Введіть рядок: ")
text = text.lower()
text_vowels = []
text_consonants = []
vowels = "aeiou"

for letter in text:
    if letter in string.ascii_lowercase:
        if letter in vowels:
            text_vowels.append(letter)
        else:
            text_consonants.append(letter)

print(f"Кількість голосних літер: {len(text_vowels)}")
print(f"Кількість приголосних літер: {len(text_consonants)}")
