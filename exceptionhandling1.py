#a=int(input("enter"))
#b=int(input("enter"))
#print(a/b)
#if we do this code we get error


#to handle error ie occured we use expection handling
a=int(input("enter a:"))
b=int(input("enter b:"))

try:
   print(a/b)
except:
    print("b cannot be 0")
print("after the error")

print("__________")