# Logical operators
x, y = 10, 5
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\nLogical AND operators")
x, y, z = 10, 5, 4
if x < y and y < z:
    print('YES')
else:
    print('NO')

print("\nLogical OR operators")
x, y, z = 10, 5, 4
if x > y or y > z:
    print('YES')
else:
    print('NO')
