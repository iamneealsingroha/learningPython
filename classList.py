z = ["Aksh", "Aashish", "Ishita", "Mohak", "Udit", "Yuvraj"]
print(z)
y = int(input("How many names do you want to add? "))
for i in range(y):
    x = int(input("Enter the position where you want to add the name: "))
    w = input("Enter the name you want to add: ")
    v = x-1
    z.insert(v, w)
    print(z)
u = int(input("How many names do you want to remove? "))
for i in range(u):
    t = input("Enter the name you want to remove: ")
    z.remove(t)
    print(z)
print("The final list of names is: ", z)
