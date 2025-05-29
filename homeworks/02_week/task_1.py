# ДЗ 2.1. Виведення числа в стовпчик
input_number = int(input("Please enter a 4-digit number: "))

if not 1000 <= input_number <= 9999:
    print("Please enter a valid 4-digit number.")
else:
    # Solution 1 (used // and % operators)
    # digit_4 = input_number % 10
    # input_number //= 10
    #
    # digit_3 = input_number % 10
    # input_number //= 10
    #
    # digit_2 = input_number % 10
    # input_number //= 10
    #
    # digit_1 = input_number % 10

    # Solution 2 (used divmod())
    num, digit_4 = divmod(input_number, 10)
    num, digit_3 = divmod(num, 10)
    num, digit_2 = divmod(num, 10)
    num, digit_1 = divmod(num, 10)
    print(digit_1)
    print(digit_2)
    print(digit_3)
    print(digit_4)
