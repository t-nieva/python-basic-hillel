from human import Human


class Student(Human):

    def __init__(self, first_name, last_name, gender, age, record_book):
        super().__init__(first_name, last_name, gender, age)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f"\nRecord book: {self.record_book}"
