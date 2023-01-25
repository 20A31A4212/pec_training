n = int(input("enter:"))
if n > 0 and n < 20:
    if n % 2 == 0:
        print("weird num")
    else:
        print("normal num")
elif n >= 20 and n < 30:
    print("normal num")
elif n >= 30:
    if n % 2 != 0:
        print("normal num")
    else:
        print("weird num")
else:
    print("invalid")

