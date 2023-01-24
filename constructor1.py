
#syntax of constructor--> def __init__(self):-->default constructor
class Student:
    student_name=""
    def __init__(self,name): #constructor is used to initialize class variables
        print("obj created")
        print(name)
s1=Student("mukesh")


print("_________________")

#class Teacher:
    #teacher_name="No name"
    #def __init__(self,name):
        #print("object created")
        #print(teacher_name) #here class variables are not accessible in constructor
#s2=Teacher("ramesh")



class Myname:
    myname="No name"
    def __init__(self,name):
        print("obj created")
        print(self.myname)#here by using self. we can access class variables in constructor
s3=Myname("muk")

print("_____________________")

