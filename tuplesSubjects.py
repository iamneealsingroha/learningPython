subjects = ("Math", "Computers", "English", "Physics", "Chemistry")
print(subjects)
a = input("Enter a subjest to add:")
subjects = subjects + (a,)
print(subjects)
b = int(input("Enter the first number to the range of subjects to keep:"))
c = int(input("Enter the last number to the range of subjects to keep:"))
subjects1=subjects[b-1:c]
print(subjects1)
print(subjects)
d = input("Do you want to keep more subjects? (y/n):")
if d == "y":
    e = int(input("Enter the first number to the range of subjects to keep:"))
    f = int(input("Enter the last number to the range of subjects to keep:"))
    subjects2=subjects[e-1:f]
    print(subjects2)
    subjects = subjects1 + subjects2
else:    
    print(subjects)
print(subjects)