# Напишіть програму, яка запитує у користувача суму у євро і потім виводить:
# мінімальну кількисть купюр та мінімальну кількість монет для того, щоб
# отримати цю суму у євро. Зверніть увагу на те, що банкноти євро мають
# номінали: 5, 10, 20, 50, 100, 200 та 500 евро. А монети: 1 та 2 євро,
# 1, 2, 5, 10, 20 та 50 євроцентів.
# Крім того треба надрукувати кількість кожного номіналу котрий
# використовується для отримання даної суми.
# * Бажано, щоб суму можна було вводити як через крапку так і через кому.

# Приклад: Введіть суму: 347,78
# Кількість банкнот: 5
# Кількість монет: 7
# Склад суми:
# 1 x 200
# 1 x 100
# 2 x 20
# 1 x 5
# 2 x 1 # тут помилка! Для монет євро => правильно 1 х 2
# 1 x 0.5
# 1 x 0.2
# 1 x 0.05
# 1 x 0.02
# 1 x 0.01


def find_money(amount: float, money: list[float]):
    """
    Returns the largest denomination (banknote or coin) from the given list
    that is less than or equal to the specified amount.

    Parameters:
        amount (float): The remaining amount to be broken down.
        money (list[float]): A list of available denominations,
                             preferably sorted in descending order.

    Returns:
        float | None: The highest suitable denomination that does not exceed the amount,
                      or None if no such denomination is available.
    """
    for item in money:
        if amount >= item:
            return item
    return None


def print_composition(items_to_print: list[float]):
    """
    Prints the count of each denomination used in the format 'count x denomination'.

    Parameters:
        items_to_print (list[float]): A list of used denominations
                                      (banknotes or coins).

    Returns:
        None
    """
    if items_to_print:
        for_print = []
        for item in items_to_print:
            _count = items_to_print.count(item)
            if (_count, item) not in for_print:
                for_print.append((_count, item))
        for item in for_print:
            print(f"{item[0]}x{item[1]}")


input_euros = input("Enter the amount, euros: ")

if "," in input_euros:
    input_euros = input_euros.replace(",", ".")

amount = float(input_euros)
banknotes = sorted([500, 200, 100, 50, 20, 10, 5], reverse=True)
euro_coins = sorted([2, 1], reverse=True)
coins_eurocents = sorted([0.50, 0.20, 0.10, 0.05, 0.02, 0.01], reverse=True)

list_of_banknotes = []
list_of_coins = []
list_of_eurocents = []

while True:
    found_banknote = find_money(amount, banknotes)
    if found_banknote:
        list_of_banknotes.append(found_banknote)
        amount -= found_banknote
    else:
        found_coins_euros = find_money(amount, euro_coins)
        if found_coins_euros:
            list_of_coins.append(found_coins_euros)
            amount -= found_coins_euros
        else:
            found_eurocents = find_money(amount, coins_eurocents)
            if found_eurocents:
                list_of_eurocents.append(found_eurocents)
                amount -= found_eurocents
            else:
                if 0 < round(amount, 2) <= 0.01:
                    list_of_eurocents.append(0.01)
                break

print(f"Number of banknotes: {len(list_of_banknotes)}")
print(f"Number of coins: {len(list_of_coins) + len(list_of_eurocents)}")
print("Composition of the amount:")
print_composition(list_of_banknotes)
print_composition(list_of_coins)
print_composition(list_of_eurocents)
