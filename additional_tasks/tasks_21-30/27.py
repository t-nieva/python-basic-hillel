# Напишіть програму, яка за числом n від 1 до 9 виводить на екран n
# пінгвінів. Зображення одного пінгвіна має розмір 5х9 символів.
# Вхідні дані:
# Вводиться натуральне число.
# Вихідні дані:
# Виводиться введена кількість пінгвінів у рядок.
# Примітка:
# Врахуйте, що виведення даних на екран робиться рядковим, а не попінгвінним.
#
# У деяких мовах програмування символ зворотного слеша “\” у текстових
# рядках має спеціальне значення. Щоб включити до текстового рядка
# такий символ, його потрібно повторити двічі. Наприклад, для виведення на екран
# одного такого символу можна використовувати такий код: print("\\").
#    _~_
#   (o o)
#  /  V  \
# /(  _  )\
#   ^^ ^^
#
# Приклад:
# Введить кількість пінгвінів: 3
#     _~_        _~_        _~_
#    (o o)      (o o)      (o o)
#   /  V  \    /  V  \    /  V  \
#  /(  _  )\  /(  _  )\  /(  _  )\
#    ^^ ^^      ^^ ^^      ^^ ^^

penguins_number = int(input("Введить кількість пінгвінів (від 1 до 9):"))
if 1 <= penguins_number <= 9:
    penguin = ["_~_", "(o o)", "/  V  \\", "/(  _  )\\", "^^ ^^"]
    for item in penguin:
        print(f"{item:^12}" * penguins_number)
else:
    print("Invalid input")
