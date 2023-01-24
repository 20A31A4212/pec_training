#######################HIERARCHICAL-INHERITANCE############################3

class Person:
    name="madhu"
    gender="f"
    age=19


class Student(Person):
    roll_num="20a31a4212"
    branch="cse"

class Faculty(Person):
    salary=10000
    subject="chemistry"
    reportsTo="reports to vc"
class VC(Person):
    def give_salary(self):
        print("gives salary to teachers or faculty")
    def take_fees(self):
        print("takes fees from students")
#obj created for VC
obj1=VC()
obj1.give_salary()
print(obj1.name)
print(obj1.gender)
#obj created for Faculty
obj2=Faculty()
print(obj2.salary)
print(obj2.age)
#obj created for Student
obj3=Student()
print(obj3.roll_num)
print(obj3.name)

