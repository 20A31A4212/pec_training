#Inheritance:clild class inherit or takes properties from parent class
"""Types of inheritance:1.single level interitance
                        2.multi level inheritance
                        3.hierarchical inheritance
                        4.multiple inheritance
                        5.hybrid inheritance
"""
#######SINGLE LEVEL INHRITANCE########
class A:
    name="madhu"
    age=36



class B(A):
    age=10

obj=B()
print(obj.age)
print(obj.name)

print("______________")

class A:
    name="madhu"
    age=36



class B(A):
    age=10

obj=B()
obj.name="ramesh"
print(obj.age)
print(obj.name)