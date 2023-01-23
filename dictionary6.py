l = []
d = {}
for i in range(2):
    d.update({
        "key1": input("enter key 1:"),
        "key2": input("enter key 2:")
    })
    l.append(d)
print(d)