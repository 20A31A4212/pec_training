
class Student:
    student_name="No name"
    def __init__(self,name):
        self.student_name=name
s1=Student("mukesh")
s2=Student("ramesh")
print(s2.student_name)


print("________________")

#updating the student_name
class Student:
    student_name = "No name"

    def __init__(self, name):
        self.student_name = name

    def update_name(self, new_name):
        self.student_name = new_name


s1 = Student("mukesh")
s2 = Student("ramesh")
s3 = Student("rakesh")

print(s2.student_name)  # before updating student_name s2
s2.update_name("ramesh reddy")
print(s2.student_name)  # after updating student_name s2