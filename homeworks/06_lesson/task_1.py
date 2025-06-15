import string

letters = list(string.ascii_letters)

user_input = input("Enter two letters separated by a dash " "(e.g., 'a-c' or 's-H'): ")
letter_range = user_input.split("-")

start_end_indexes = [letters.index(letter) for letter in letter_range]
start = start_end_indexes[0]
end = start_end_indexes[1] + 1

result = letters[start:end]
print("".join(result))
