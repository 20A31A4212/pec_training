l=[56,43,78,345,789,"hello",[1,2,3,4]]
#printing index of 78 using for loop

k=78
for i in range(len(l)):
    if k==l[i]:
        print(i)
        temp=True
        break
if temp == False:
    print("ele not found")

print("______________")

l=[]
for i in range(10):
    l.append(i*i)
print(l)

print("_____________")

l=[x for x in range(0,10)]
print(l)

print("_____________")

l=[x*x for x in range(0,10)]
print(l)

print("_____________")

l=[num for num in range(0,51) if num%2!=0]
print(l)

print("_____________")

l=[num for num in range(0,101) if num%7==0 and num%11==0] #numbers that are divisible by 7 and 11 with in range of 0-100
print(l)