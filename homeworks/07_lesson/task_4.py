def common_elements():
    multiples_of_3 = {el for el in range(100) if el % 3 == 0}
    multiples_of_5 = {el for el in range(100) if el % 5 == 0}
    return multiples_of_3 & multiples_of_5


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Ok")
