import random

len_list = random.randint(3, 10)
my_list = []

while len_list:
    item = random.randint(0, 100)
    my_list.append(item)
    len_list -= 1

new_list = [my_list[0], my_list[2], my_list[-2]]

print(my_list)
print(new_list)
