from student import Student
from group import Group, TooManyStudentsError

gr = Group("PD1")
st1 = Student(
    gender="Male", age=30, first_name="Steve", last_name="Jobs", record_book="AN142"
)

st2 = Student(
    gender="Female", age=25, first_name="Liza", last_name="Taylor", record_book="AN145"
)
gr.add_student(st1)
gr.add_student(st2)

assert str(gr.find_student("Jobs")) == str(st1), "Test1"
assert gr.find_student("Jobs2") is None, "Test2"
assert (
    isinstance(gr.find_student("Jobs"), Student) is True
), "Метод поиска должен возвращать экземпляр"

# gr.delete_student("Taylor")
# print(gr)  # Only one student
#
# gr.delete_student("Taylor")  # No error!

# task 14.1
print("*" * 10, "task 14.1", "*" * 10)
students = [
    Student(
        gender="Female",
        age=25,
        first_name="Liza3",
        last_name="Taylor",
        record_book="AN145",
    ),
    Student(
        gender="Female",
        age=25,
        first_name="Liza4",
        last_name="Taylor",
        record_book="AN145",
    ),
    Student(
        gender="Female",
        age=25,
        first_name="Liza5",
        last_name="Taylor",
        record_book="AN145",
    ),
    Student(
        gender="Female",
        age=25,
        first_name="Liza6",
        last_name="Taylor",
        record_book="AN145",
    ),
    Student(
        gender="Female",
        age=25,
        first_name="Liza7",
        last_name="Taylor",
        record_book="AN145",
    ),
    Student(
        gender="Female",
        age=25,
        first_name="Liza8",
        last_name="Taylor",
        record_book="AN145",
    ),
    Student(
        gender="Female",
        age=25,
        first_name="Liza9",
        last_name="Taylor",
        record_book="AN145",
    ),
    Student(
        gender="Female",
        age=25,
        first_name="Liza10",
        last_name="Taylor",
        record_book="AN145",
    ),
    Student(
        gender="Female",
        age=25,
        first_name="Liza11",
        last_name="Taylor",
        record_book="AN145",
    ),
]
for student in students:
    try:
        gr.add_student(student)
        # print(f"Student {student.first_name} added.")
    except TooManyStudentsError as e:
        print(f"Error adding {student.first_name}: {e}")

print(f"\nTotal students in group: {len(gr.group)}")

# task => 14.2
print("*" * 10, "task 14.2", "*" * 10)
assert gr.find_student("Jobs") == st1
print("Ok")
