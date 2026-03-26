z = ["mango","apple", "banana", "watermelon","litchi", "orange", "papaya"]
for i in z:
    print(i)
print("Index 4:", z[3])
print("Index 2:", z[1])
print("Index 1:", z[0])
print("Index 5 and 7:", z[4], z[6])
print("Range 3 to 6 ", z[2:6])
for x in range(0, 7):
    y = z[x]
    print("Position", x+1, ":", y)
print("Length of the list:", len(z))
print("Current list:", z)
w = input("Fruit to enter at the end of the list:")
z.append(w)
print("Updated list:", z)
v = int(input("Position to insert the fruit:"))
u = input("Fruit to insert at the position:")
z.insert(v-1, u)
print("Updated list:", z)
t = int(input("Position to remove the fruit:"))
z.pop(t-1)
print("Updated list:", z)
s = int(input("First number of range:"))
r = s-1
q= int(input("Second number of range:"))
p = q-1
print("Removing range", s, "to", q)
del z[r:p]
print("Updated list:", z)
o = input("Fruit to remove from the list:")
z.remove(o)
print("Updated list:", z)