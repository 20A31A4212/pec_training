db=[{"abc@example.com":"abc"},
    {"xyz@example.com":"123"},
    {"a123@example.com":"ugyfth"},
    {"zxc@example.com":"123456"},
    ]
print(db)
username=input("enter username:")
password=input("enter password:")

temp={username:password}
if temp in db:
    print("found")
else:
    print("not found")