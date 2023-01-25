#same methodname diff signature "method overloading"

def m1(a,b):
    print(a+b)

def m1(a,b,c):
    print(a+b+c)

m1(1,2,3)
#m1(1,2) gives error(missing 1 parameter) becoz m1 is overloaded with 3 parameters

#same methodname in diff class "method overriding"

class A:
    def m1(self):
        print("in class A")

class B(A):
    def m1(self):
        print("in class B")


obj=B()
obj.m1()