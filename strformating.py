first="Mr.X is"
age=30
last="years old"
#without using formatting
print(first+str(age)+last)

#using formatting 1st method
print("Mr.X is {} years old".format(age))

num=3.14
print("the square of {} is {}".format(num,num*num))
#gives 2 decimal nums after point
print("the square of {} is {:.2f}".format(num, num*num))
#gives 10 spaces
print("the square of {:10} is {:.2f}".format(num, num*num))


#2nd method of formatting
num=13.14
print(f"the square of {num} is {num*num}")

print(f"the square of {num} is {num*num:.2f}")

print(f"the square of {num:10} is {num*num:.2f}")