rows=3
col=3
arr1=[]

for i in range(rows):
    element=[]
    for j in range(col):
        element.append(int(input("enter ele:")))
    arr1.append(element)
print(arr1)

rows=3
col=3
arr2=[]

for i in range(rows):
    element=[]
    for j in range(col):
        element.append(int(input("enter ele:")))
    arr2.append(element)
print(arr2)

res=[[0 for j in range(col)] for i in range(rows)]
for i in range(rows):
    for j in range(col):
        res[i][j]=arr1[i][j]+arr1[i][j]

print(res)