# ДЗ 2.1. Виведення числа в стовпчик
input_digit = int(input("Please enter a 4-digit number: "))
digit_1 = None
digit_2 = None
digit_3 = None
digit_4 = None

# Solution 1 (used // and % operators)
# if 0 <= input_digit % 10 <=9:
#     digit_4 = input_digit % 10
# input_digit //= 10
#
# if 0 <= input_digit % 10 <=9:
#     digit_3 = input_digit % 10
# input_digit //= 10
#
# if 0 <= input_digit % 10 <=9:
#     digit_2 = input_digit % 10
# input_digit //= 10
#
# if 0 <= input_digit % 10 <=9:
#     digit_1 = input_digit % 10

# Solution 2 (used divmod())
integer_part, fractional_part = divmod(input_digit, 10)
if 0 <= fractional_part <=9:
    digit_4 = fractional_part
new_digit = integer_part

integer_part, fractional_part = divmod(new_digit, 10)
if 0 <= fractional_part <=9:
    digit_3 = fractional_part
new_digit = integer_part

integer_part, fractional_part = divmod(new_digit, 10)
if 0 <= fractional_part <=9:
    digit_2 = fractional_part
new_digit = integer_part

integer_part, fractional_part = divmod(new_digit, 10)
if 0 <= fractional_part <=9:
    digit_1 = fractional_part
new_digit = integer_part

print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)
