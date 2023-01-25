print(list(range(1,10)))
#range(start:stop:step size)
print(list(range(1,10,2)))

print("_______________")

for i in range(1,16):
    print(i) #default value of end is \n

print("________________")

lst=[45,55,65,75,85]
for i in lst:
    print(i)

print("______________")

lst=[1,2,3,4]
for i in lst:
    print(i*i)

print("______________")

lst=[78,65,79,34]
list(range(0,len(lst)))
for i in range(0,len(lst)):
    print(i,lst[i])
