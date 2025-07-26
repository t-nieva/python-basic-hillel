# Напишіть програму, яка запитує у користувача рядок і визначає, чи є вiн
# панграмою. Панграма - це фраза, що містить усі літери алфавіту. Програма
# повинна ігнорувати регістр літер та пробіли під час перевірки панграми.
# Виведіть відповідне повідомлення на екран за допомогою команди print.
# Розв'язати задачу для латиниці.
#
# Приклад:
# Введіть рядок: The quick brown fox jumps over the lazy dog
# Рядок є панграмою.

import string

text = input("Введіть фразу: ")
text = text.lower()
letters_in_text = {char for char in text if char.isalpha()}

if letters_in_text >= set(string.ascii_lowercase):
    print("Це панграма.")
else:
    print("Це не панграма.")
