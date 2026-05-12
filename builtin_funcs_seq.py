# Indexing
number = [1, 2, 3, 4, 5, 6]
print("Element at index 2:", number[2])
text = "Shreeharsh"
print(text[-1])
print(text[-2])
print(text[-3])

print("\nRepetition")
# Repetition
text_rep = "CorePython"
print("Repeating the text 3 times:", text_rep * 3)
numbers_rep = [1, 2, 3, 4, 5]
print("Repeating the number 3 times:", numbers_rep * 3)
string_full = "CorePython"
s = string_full[5:7] * 3
print("Slice repetition:", s)

print("\nGeneral purpose Functions")
# General purpose Functions
text_gen = 'Python'
print("Type of text:", type(text_gen))

print("\nMathematical Functions")
# Mathematical Function
num_val = -25
print("Absolute value:", abs(num_val))
print("Power value of (2^3):", pow(2, 3))
print("Rounded value of 5.68345 up to 2 decimal:", round(5.68, 2))

print("\nSEQUENCE FUNCTION")
# Sequence Function
numbers_seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Length of numbers:", len(numbers_seq))
print("Maximum value:", max(numbers_seq))
print("Minimum value:", min(numbers_seq))
print("Sum of numbers:", sum(numbers_seq))
print("Sorted numbers:", sorted(numbers_seq, reverse=True))

print("\nString functions")
# String functions
text_str = "firstname lastname"
print("Uppercase:", text_str.upper())
print("Lowercase:", text_str.lower())
print("Replaced Text:", text_str.replace("lastname", "firstname"))

print("\nConversion functions")
# Conversion functions
num_str = "100"
float_num = "25.67"
print("String to int:", int(num_str))
print("String to float:", float(num_str))
text_base = "Shreeharsh"
num_list = [1, 2, 3, 4, 5]
print("List from string:", list(text_base))
print("Tuple from list:", tuple(num_list))

print("\nLogical and Comparison Functions")
# Logical and Comparison Functions
bool_list = [True, False, True]
print("Are all values True?", all(bool_list))
print("Is any value True?", any(bool_list))

print("\nUtility Function")
# Utility Function
print("Range as list:", list(range(4, 28, 3)))
