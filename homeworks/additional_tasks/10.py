# Напишіть програму, яка запитує у користувача ціле позитивне число і перевіряє,
# чи є воно простим. Просте число - це число, яке ділиться тільки на 1 і на само
# себе без залишку. Використовуйте цикл і перевірку поділу числа на всі числа
# від 2 до N-1 для вирішення задачі.
# Виведіть відповідне повідомлення на екран за допомогою print.
#
# Приклад:
# Введіть позитивне число: 17
# Число 17 є простим.

n = int(input("Введіть позитивне число: "))
# Простими вважаються числа від 2 і вище (0 і 1 — не прості)
if n < 2:
    print(f"Число {n} не є простим.")
else:
    is_prime = True
    i = 2
    while i < n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(f"Число {n} є простим.")
    else:
        print(f"Число {n} не є простим.")
