################################HYBRID-INHERITANCE###################################
#(combination of any 2 inheritances known as hybrid inheritance)
class A:
    def parent(self):
        print("'A' is parent of child 'B',child 'C'")

class B(A):
    def pc1(self):
        print("'B' is child of parent 'A' and parent of child 'D'")

class C(A):
    def pc2(self):
        print("'C' is child of parent 'A' and parent of child 'D'")

class D(B,C):
    def child(self):
        print("'D' is child of parent 'B' and parent 'C'")

obj1=D()
obj1.parent()
obj1.pc1()
obj1.pc2()
obj1.child()

