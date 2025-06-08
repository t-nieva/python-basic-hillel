import random

list_len = random.randint(3, 10)
my_list = [random.randint(0, 100) for item in range(list_len)]
new_list = [my_list[0], my_list[2], my_list[-2]]

print(my_list)
print(new_list)
