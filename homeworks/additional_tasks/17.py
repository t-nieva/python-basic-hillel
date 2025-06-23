# Напишіть програму, яка запитує у користувача рядок і перетворює його,
# видаляючи всі голосні літери з рядка. Використовуйте метод replace() для
# заміни голосних літер на порожній рядок. Виведіть перетворений рядок на
# екран за допомогою команди print.
#
# Приклад:
# Введіть рядок: Hello, world!
# Результат: Hll, wrld!

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
for letter in vowels:
    text = text.replace(letter, "")

print(f"Result: {text}")
