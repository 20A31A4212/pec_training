
#################################MULTIPLE-INHERITANCE#########################

#diamond problem

class P1:
    def m1(self):
        print("parent1")


class P2:
    def m1(self):
        print("parent2")


class C(P1,P2):
    pass

obj=C()
obj.m1()


print("_________________")


class P1:
    def m1(self):
        print("parent1")


class P2:
    def m1(self):
        print("parent2")


class C(P2,P1):
    pass

obj=C()
obj.m1()