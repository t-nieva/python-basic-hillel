result = 0
num1 = float(input("What's the first number: "))
operation = input("+\n-\n*\n/\n Pick the operation: ").strip()
num2 = float(input("What's the next number?: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
else:
    print("Invalid operation selected.")

print(result)
