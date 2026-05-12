# Python Program to create dictionary
d = {}
print("Empty dict:", d)
d[1] = 'Shreeharsh'
d[2] = 'Patil'
print("Updated dict:", d)

print("\nAccess and view data methods")
d2 = {17: 'Shreeharsh', 5: 'Patil', 20: 'Verna', 11: 'Goa'}
print("Dict content:", d2)
print("Access key 17:", d2[17])

print("Dictionary keys:", d2.keys())
print("Dictionary values:", d2.values())

print("\nModifying dictionaries")
d2[11] = 'India'
print("Updated value at key 11:", d2)

del d2[11]
print("Dict after deleting key 11:", d2)
