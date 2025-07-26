# Напишіть програму, яка запитує у користувача рядок і визначає, чи містить
# він тільки унікальні символи. Якщо всі символи в рядку унікальні, виведіть
# відповідне повідомлення на екран. В іншому випадку виведіть повідомлення
# про те, які символи повторюються. Не використовуйте множини для
# перевірки унікальності символів.
#
# Приклад:
# Введіть рядок: Python
# Усі символи у рядку унікальні.
# Введіть рядок: Hello Konal
# Символи 'l' і 'o' повторюються.

text = input("Enter a string: ")
repeated_letters = ""

for letter in text:
    if text.count(letter) > 1 and letter not in repeated_letters:
        repeated_letters += letter

if not repeated_letters:
    print("All characters in a string are unique.")
elif len(repeated_letters) == 1:
    print(f"The character '{repeated_letters}' is repeated.")
else:
    repeated_list = list(repeated_letters)
    msg = ", ".join(f"'{ch}'" for ch in repeated_list[:-1])
    msg += f" and '{repeated_list[-1]}'"
    print(f"The characters {msg} are repeated.")
