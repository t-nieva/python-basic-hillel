list_1 = [12, 3, 4, 10]
list_2 = [1]
list_3 = []
list_4 = [12, 3, 4, 10, 8]

def move_item(my_list):
    if len(my_list) == 0:
        print(my_list)
    else:
        my_list.insert(0, my_list.pop())
        print(my_list)

move_item(list_1)
move_item(list_2)
move_item(list_3)
move_item(list_4)
