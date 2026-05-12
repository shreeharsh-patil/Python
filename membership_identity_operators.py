# Membership in operator
names = ["Shreeharsh", "Tusar", "Shishir", "Ankit", "Sneden"]
print("Iterating over names:")
for name in names:
    print(name)

print("\nMembership not in operator")
list1 = [2, 3, 1, 4, 5, 6]
string1 = "My name is Shreeharsh"
tuple1 = (11, 44, 32, 1, 3)
print("5 not in list1:", 5 not in list1)
print("'Shreeharsh' not in string1:", "Shreeharsh" not in string1)
print("88 not in tuple1:", 88 not in tuple1)

print("\nIs Identity operator")
a = 5
b = 5
if a is b:
    print("a and b have same identity")
else:
    print("a and b do not have same identity")

print("\nIs not Identity operator")
a = [1, 0, 2]
b = [1, 0, 2]
c = a
print("a is not b:", a is not b)
print("a is not c:", a is not c)
