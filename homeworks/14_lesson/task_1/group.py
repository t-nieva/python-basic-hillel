class TooManyStudentsError(Exception):
    pass


class Group:

    def __init__(self, number: str):
        self.number = number
        self.group = set()  # множина об'єктів Student

    def add_student(self, student):
        if len(self.group) >= 10:
            raise TooManyStudentsError(
                "Sorry, the number of students cannot be more than 10."
            )
        self.group.add(student)

    def delete_student(self, last_name):
        found_student = self.find_student(last_name)
        if found_student:
            self.group.remove(found_student)
            return True
        return False

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n\n".join(str(student) for student in self.group)
        return f"Number:{self.number}\n\n{all_students}"
