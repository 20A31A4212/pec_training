db=[{"abc@example.com":"abc"},
    {"xyz@example.com":"123"},
    {"a123@example.com":"ugyfth"},
    {"zxc@example.com":"123456"},
    ]
print(db)


for i in db:
    print(i.items())
    print(i.keys())
    print(i.values())