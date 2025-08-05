# Створити програму-калькулятор у вигляді класу та кілька методів, як мінімум
# додавання, віднімання, ділення, множення, зведення в ступінь та вилучення
# квадратного кореня. Обернути кожен метод у блок try/except і зробити обробку
# кількох винятків, як мінімум ділення на 0. Створити свій виняток, наприклад,
# зведення в негативний ступінь.
import math


class NegativeDegree(Exception):

    def __init__(self, message="Зведення у негативний ступінь"):
        super().__init__(message)


class Calculator:

    def __init__(self, start=0):
        self.value = start

    def __str__(self):
        return f"Результат: {self.value}"

    def __add__(self, other):
        try:
            return Calculator(self.value + other)
        except TypeError:
            return "Не можна складати цифри та літери!"

    def __sub__(self, other):
        try:
            return Calculator(self.value - other)
        except TypeError:
            return "Не можна від цифри віднімати літери!"

    def __mul__(self, other):
        try:
            return Calculator(self.value * other)
        except TypeError:
            return "Не можна множити число на літери!"

    def __truediv__(self, other):
        try:
            return Calculator(self.value / other)
        except ZeroDivisionError:
            print("На нуль ділити не можна.")
            return None
        except TypeError:
            return "Не можна ділити на літери!"

    def __pow__(self, power, modulo=None):
        try:
            if power >= 0:
                return Calculator(self.value**power)
            else:
                raise NegativeDegree()
        except NegativeDegree:
            return "Зведення у негативний ступінь заборонено!"

    def sqrt(self):
        try:
            if self.value < 0:
                raise ValueError("Не можна знайти корінь з від’ємного числа!")
            return math.sqrt(self.value)
        except ValueError as e:
            return str(e)


if __name__ == "__main__":
    calc = Calculator(10)
    result = calc + 5
    print(result)  # Результат: 15

    result = result - 3
    print(result)  # Результат: 12

    result = result * 2
    print(result)  # Результат: 24

    result = result / 0  # На нуль ділити не можна.
    print(result)

    result = Calculator(2) ** -1
    print(result)  # Зведення у негативний ступінь заборонено!

    result = Calculator(-4).sqrt()
    print(result)  # Не можна знайти корінь з від’ємного числа!


# Solution

# class Negative_degree(Exception):
#     def __init__(self, message='Зведення у негативний ступінь'):
#         super().__init__(message)
#
#
# class Calculator(int):
#
#     def __init__(self, var):
#         self.var = var
#
#     def __add__(self, other):
#         try:
#             return Calculator(self.var + other)
#         except TypeError:
#             return 'Не можна складати цифри та літери!'
#
#     def __sub__(self, other):
#         try:
#             return Calculator(self.var - other)
#         except TypeError:
#             return 'Не можна від цифри відібрати літери!'
#
#     def __pow__(self, power, modulo=None):
#         try:
#                 if power >= 0:
#                     return Calculator(self.var ** power)
#                 else:
#                     raise Negative_degree()
#         except Negative_degree:
#             return 'Зведення у негативний ступінь заборонено!'
#
#     def __truediv__(self, other):
#         try:
#             return Calculator(self.var / other)
#         except ZeroDivisionError:
#             return 'Не можна ділити на нуль!'
#         except TypeError:
#             return 'Не можна ділити на літери!'
