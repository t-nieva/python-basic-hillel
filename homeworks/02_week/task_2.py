# ДЗ 2.2. Необхідно "перевернути" 5-ти значне число
input_number = int(input("Please enter a 5-digit number: "))

input_number, d1 = divmod(input_number, 10)
input_number, d2 = divmod(input_number, 10)
input_number, d3 = divmod(input_number, 10)
input_number, d4 = divmod(input_number, 10)
input_number, d5 = divmod(input_number, 10)
d1 *= 10000
d2 *= 1000
d3 *= 100
d4 *= 10
res = d1 + d2 + d3 + d4 + d5
print(res)
