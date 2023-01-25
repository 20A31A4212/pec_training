def add(num1,num2):
    res=num1+num2
    return res
print(add(10,20))



print("_____________")

def addition(num1,num2=0):   #default value functions
    result=num1+num2
    return result
a=10
b=10
print(addition(a))

print("_____________")

def add(a,b,c,d):    #keyword arg
    print(a,b,c,d)
add(10,20,30,40)

print("_____________")

def addition(num1=1,num2=1):
    result=num1+num2
    return result
a=10
b=10
print(addition(a))

print("______________")

#variable length argument=it'll take any no. of arguments,datatype is tuple
def add(a,b,*abc):
    res1=1
    for i in abc:
        res1=i
    return res1
print(add(10,20,30,40,50))