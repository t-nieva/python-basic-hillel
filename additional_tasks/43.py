# Створіть клас BankAccount для надання банківського рахунку. Клас повинен
# мати атрибути account_number (номер рахунку) та balance (баланс), а також
# методи deposit() для внесення грошей на рахунок і withdraw() для зняття
# грошей з рахунку. Потім створіть екземпляр класу BankAccount, внесіть на
# рахунок деяку суму і зніміть частину грошей. Виведіть баланс, що залишився.
# Не забудьте передбачити варіант, при якому при знятті баланс може стати
# меншим за нуль. У цьому випадку йти в мінус не будемо, замість чого
# повертатимемо повідомлення "Недостатньо коштів на рахунку".


class BankAccount:

    def __init__(self, account_number=0, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        if amount < 0:
            print("Invalid input.")
        else:
            self.balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            print("Invalid input.")
        elif self.balance < amount:
            print("Недостатньо коштів на рахунку")
        else:
            self.balance -= amount


customer_1 = BankAccount(1)
customer_1.deposit(100)
customer_1.withdraw(25)
customer_1.withdraw(20000)
print(
    f"Залишок на рахунку '{customer_1.account_number}' становить: {customer_1.balance}"
)


# Solution
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount < 0:
#             print("Неправильна сума. Операція не виконана")
#         else:
#             self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance - amount < 0:
#             print("Недостатньо коштів на рахунку")
#         else:
#             self.balance -= amount
#
#
# my_acc = BankAccount("DE34667678EU", 1000)
# my_acc.deposit(200)
# my_acc.withdraw(2000)
# my_acc.withdraw(500)
# print(f"Залишок на рахунку '{my_acc.account_number}' становить: {my_acc.balance}")
