# ДЗ 2.2. Необхідно "перевернути" 5-ти значне число
input_digit = int(input("Please enter a 5-digit number: "))
output = ""

output += str(input_digit % 10)
input_digit //= 10

output += str(input_digit % 10)
input_digit //= 10

output += str(input_digit % 10)
input_digit //= 10

output += str(input_digit % 10)
input_digit //= 10

output += str(input_digit % 10)
input_digit //= 10

print(output)
