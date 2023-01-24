##############METHOD OVERRIDING(RUN TIME POLYMORPHISM)########################
# (inheritance concept is  needed here)
class A:
    def method_1(self,a,b):
        print("sum of 2 nums:",a+b)
class B(A):
    def method_1(self,a,b):
        print("mul of 2 nums:",a*b)
obj=B()
obj.method_1(10,20)

##############METHOD OVERLOADING(COMPILE TIME POLYMORPHISM)########################
# (inheritance concept is not needed here)
class A:
    def method_1(self,a,b):
        print("sum of 2 nums:",a+b)
class B(A):
    def method_1(self,a,b):
        print("diff of 2 nums:",a-b)
    def method_1(self,abc): #here method 1 is being updated
        print("value is",abc)
obj=B()
obj.method_1(10) #method with 1 arg



class A:
    def method_1(self,a,b):
        print("sum of 2 nums:",a+b)
class B(A):
    def method_1(self,abc):
        print("value is",abc)
    def method_1(self,a,b): #here method 1 is being updated
        print("diff of 2 nums:",a-b)
obj=B()
obj.method_1(10,20) #method with 1 argument