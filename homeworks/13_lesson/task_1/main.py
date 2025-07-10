from student import Student
from group import Group

st1 = Student(
    gender="Male", age=30, first_name="Steve", last_name="Jobs", record_book="AN142"
)
st2 = Student(
    gender="Female", age=25, first_name="Liza", last_name="Taylor", record_book="AN145"
)

gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print("*" * 100)

assert str(gr.find_student("Jobs")) == str(st1), "Test1"
assert gr.find_student("Jobs2") is None, "Test2"
assert (
    isinstance(gr.find_student("Jobs"), Student) is True
), "Метод поиска должен возвращать экземпляр"

gr.delete_student("Taylor")
print(gr)  # Only one student

gr.delete_student("Taylor")  # No error!
