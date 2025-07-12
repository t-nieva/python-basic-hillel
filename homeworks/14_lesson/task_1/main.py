from student import Student
from group import Group

st1 = Student(
    gender="Male", age=30, first_name="Steve", last_name="Jobs", record_book="AN142"
)
st2 = Student(
    gender="Female", age=25, first_name="Liza", last_name="Taylor", record_book="AN145"
)
st3 = Student(
    gender="Female", age=25, first_name="Liza3", last_name="Taylor", record_book="AN145"
)
st4 = Student(
    gender="Female", age=25, first_name="Liza4", last_name="Taylor", record_book="AN145"
)
st5 = Student(
    gender="Female", age=25, first_name="Liza5", last_name="Taylor", record_book="AN145"
)
st6 = Student(
    gender="Female", age=25, first_name="Liza6", last_name="Taylor", record_book="AN145"
)
st7 = Student(
    gender="Female", age=25, first_name="Liza7", last_name="Taylor", record_book="AN145"
)
st8 = Student(
    gender="Female", age=25, first_name="Liza8", last_name="Taylor", record_book="AN145"
)
st9 = Student(
    gender="Female", age=25, first_name="Liza9", last_name="Taylor", record_book="AN145"
)
st10 = Student(
    gender="Female",
    age=25,
    first_name="Liza10",
    last_name="Taylor",
    record_book="AN145",
)
st11 = Student(
    gender="Female",
    age=25,
    first_name="Liza11",
    last_name="Taylor",
    record_book="AN145",
)

gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
gr.add_student(st11)
print(len(gr.group))
print("*" * 100)

assert str(gr.find_student("Jobs")) == str(st1), "Test1"
assert gr.find_student("Jobs2") is None, "Test2"
assert (
    isinstance(gr.find_student("Jobs"), Student) is True
), "Метод поиска должен возвращать экземпляр"

gr.delete_student("Taylor")
print(gr)  # Only one student

gr.delete_student("Taylor")  # No error!
