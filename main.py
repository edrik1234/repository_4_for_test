from Student import Student
from Employee import Employee
print("this is from programmer 2")
student = Student("edrian", 30, "electronics", 8 ,900)
# student.foo()

employee = Employee("John", 40, "Software Engineer", 45000)
people = [student, employee]
for person in people:
    person.printMyself()









