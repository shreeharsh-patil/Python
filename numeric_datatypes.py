# Python program for int datatype
a = -57
print("int datatype of a is", a)

# Python program for float datatype
a = 22.55e3
print("float datatype of a is", a)

# Python program to add two complex numbers
a = 2.5 + 2.5j
b = 3.0 + 0.5j
c = a + b
print("Sum of two complex numbers is", c)

print("\nExplicit datatype conversions")
# Python program for converting datatypes explicitly
a = 17.777777
print("The type conversion of float to int is", int(a))

a = 17
print("The type conversion of int to float is", float(a))

a = 17
print("The type conversion of int to complex is", complex(a))

a = 17
b = 12
print("Convert a and b into a complex number:", complex(a, b))

print("\nBase conversions to decimal")
# Python program to convert octal number to decimal number
a = 0o17
print("Convert Octal number to decimal number:", int(a))

# Python program to convert Binary number to decimal number
a = 0B1110010
print("Convert Binary number to decimal number:", int(a))

# Python program to convert Hexadecimal number to decimal number
a = 0x1c2
print("Convert Hexadecimal number to decimal number:", int(a))

print("\nString base conversions")
# Python program to convert String to decimal integer
hex_str = "1c2"
n = int(hex_str, 16)
print("Convert String to decimal integer:", n)

# Python program to convert into decimal number system
s1 = "17"
s2 = "1110010"
s3 = "1c2"
n = int(s1, 8)
print("Octal 17 in decimal number system:", n)
n = int(s2, 2)
print("Binary 1110010 in decimal number system:", n)
n = int(s3, 16)
print("Hexadecimal 1c2 in decimal number system:", n)

print("\nDecimal to other number systems")
# Python program to convert number into different number systems
a = 10
print(bin(a))
print(oct(a))
print(hex(a))
