user_input = input("Please enter a number: ")
current_digits = list(user_input)

while len(current_digits) > 1:
    product = 1
    for item in current_digits:
        product *= int(item)
    current_digits = list(str(product))

print(int(current_digits[0]))
