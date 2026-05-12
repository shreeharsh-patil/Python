# Bytes Datatype
elements = [10, 20, 30, 40, 50, 60, 70]
x_bytes = bytes(elements)
print("Iterating over Bytes array:")
for i in x_bytes:
    print(i)

print("\nBytearray datatype (Read/Display)")
# Python Program to create a Bytearray datatype
elements2 = [1, 2, 3, 4, 9, 10]
x_arr = bytearray(elements2)
for i in x_arr:
    print(i)

print("\nBytearray modification")
# Python Program to modify bytearray
elements3 = [1, 2, 3, 4, 9, 10]
x_mod = bytearray(elements3)
print("Original Array:")
for i in x_mod:
    print(i)

print("Elements after modifying:")
x_mod[2] = 6
x_mod[3] = 7
for i in x_mod:
    print(i)
