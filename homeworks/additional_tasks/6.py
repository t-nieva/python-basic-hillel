# Напишіть програму, яка запитує у користувача два логічні значення (True або
# False) і виводить результати наступних логічних операцій:

# Логічне І (and) між двома значеннями.
# Логічне АБО (or) між двома значеннями.
# Логічне НЕ (not) кожного значення.
# Результат порівняння двох значень на рівність.
# Результат порівняння двох значень на нерівність.

# Результати мають бути виведені за допомогою print. Введену строку "True"
# або "False" треба привести до булевого типу "True" або "False" і потім вже
# над булевими значеннями проводити операції.

val1_str = input("Введіть перше логічне значення (True або False): ")
val2_str = input("Введіть друге логічне значення (True або False): ")

val1 = val1_str.strip().lower() == "true"
val2 = val2_str.strip().lower() == "true"
print(f"{val1} AND {val2} = {val1 and val2}")
print(f"{val1} OR {val2} = {val1 or val2}")
print(f"NOT {val1} = {not val1}")
print(f"NOT {val2} = {not val2}")
print(f"{val1} == {val2} → {val1 == val2}")
print(f"{val1} != {val2} → {val1 != val2}")
