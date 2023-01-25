######################ARITHMETIC OPERATORS##############################

x,y=5,3
#addition(+)
print(x+y)
#subtraction(-)
print(x-y)
#multiplication(*)
print(x*y)
#division(/)
print(x/y)
#floor division
print(x//y)
#modular division(%)
print(x%y)
#exponent(**)
print(x**y)
print("__________________")

#################### Comparision(Relational) Operators ########################
a,b = 10,20
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
print("_____________________")

#################### Logical(Boolean) Operators###############################

a,b=True,False
print(a and b)
print(a or b)
print(not(a))
print("____________________")

####################BITWISE OPERATORS#########################################
a,b=10,20
print(a&b)
print(a|b)
print(~a)
print(a^b)
print("_____________________")

####################IDENTITY OPERATORS#########################################

l1=[1,2,3]
l2=[1,2,3]
print(l1 is l2)
print("___")
s1="AAIC"
s2="AAIC"
print(s1 is not  s2)

####################MEMBERSHIP OPERATORS#########################################

lst=[1,2,3,4]
print(1 in lst)#checks whether 1 is present in given lst
print("___")
d={1:"a",2:"b"}  #dictionary
print(1  not in d)   #checks whether 1 present in given dic
