# Напишіть програму, яка створює словник, що містить інформацію про
# студентів та їх оцінки. Ключами словника є імена студентів, а
# значеннями – списки оцінок. Створіть функцію calculate_average_grade,
# яка приймає словник з оцінками студентів та обчислює середній бал
# для кожного студента. Функція повинна повертати новий словник, у
# якому ключами є імена студентів, а значеннями - їх середній бал.
# Виведіть результат на екран.
#
# Приклад словника з оцінками
# grades = {
# 'Alice': [85, 90, 92],
# 'Bob': [78, 80, 84],
# 'Carol': [92, 88, 95]
# }
#
# Приклад висновку:
# {'Alice': 89.0, 'Bob': 80.67, 'Carol': 91.67}

from typing import Dict, List


def calculate_average_grade(students: Dict[str, List[float]]) -> Dict[str, float]:
    res = {}
    for std_name, std_grade in students.items():
        res[std_name] = round(sum(std_grade) / len(std_grade), 2)
    return res


grades = {}

while True:
    name = input("Enter student name: ").title()
    grades[name] = []

    while True:
        try:
            grade = float(input(f"Enter a grade for {name}: "))
            if isinstance(grade, float):
                grades[name].append(grade)
                more_grades = input(
                    "Do you want to add another grade for this student? (y/n):"
                )
                if more_grades != "y":
                    break
        except ValueError:
            print("Invalid input. Please enter a number.")
            break
    more_students = input("Do you want to add another student? (y/n):")
    if more_students != "y":
        break
print("\nGrades dictionary:")
print(grades)

print("\nAverage grades:")
print(calculate_average_grade(grades))


# Solution
# def calculate_average_grade(x):
#     k = {}
#     for key, value in x.items():
#         k[key] = round(sum(value) / len(value), 2)
#     return k
#
#
# grades = {'Alice': [85, 90, 92], 'Bob': [78, 80, 84], 'Carol': [92, 88, 95]}
# print(calculate_average_grade(grades))
