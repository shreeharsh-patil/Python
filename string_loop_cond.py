# A python program to access each element of a string in forward and reverse order using while loop
my_str = 'Shreeharsh'
n = len(my_str)
i = 0
print("Forward using while:")
while i < n:
    print(my_str[i], end=' ')
    i += 1
print()

print("Reverse approach 1:")
i = -1
while i >= -n:
    print(my_str[i], end=' ')
    i -= 1
print()

print("Reverse approach 2:")
i = 1
while i <= n:
    print(my_str[-i], end=' ')
    i += 1
print()

print("\nAccess each characters of a string using for loop")
# A python program to access characters using for loop
for char in my_str:
    print(char, end=' ')
print()
for char in my_str[::-1]:
    print(char, end=' ')
print()

print("\nChecking nature of a character")
# A python program to know the nature of a character
user_str = input('Enter a character: ')
if len(user_str) > 0:
    ch = user_str[0]
    if ch.isalnum():
        print('It is alphanumeric')
        if ch.isalpha():
            print('It is an alphabet')
            if ch.isupper():
                print('It is capital letter')
            else:
                print('It is lowercase letter')
        else:
            print('It is numeric digit')
    elif ch.isspace():
        print('It is a space')
    else:
        print('It may be a special character')

print("\nSorting a group of strings")
# A python program to sort strings into alphabetical order
str_list = []
num_to_sort = int(input('How many strings to sort? '))
for i in range(num_to_sort):
    str_list.append(input('Enter string: '))
sorted_list = sorted(str_list)
print('Sorted list:')
for item in sorted_list:
    print(item)

print("\nSearching for the position of a string")
# A python program to search for string position in group
search_list = []
num_to_search = int(input('How many strings in search pool? '))
for i in range(num_to_search):
    search_list.append(input('Enter string: '))
search_term = input('Enter the string to search: ')
found = False
for i in range(len(search_list)):
    if search_term == search_list[i]:
        print('Found at position:', i + 1)
        found = True
if not found:
    print('Not found')

print("\nString length without len()")
# Find length without using len()
manual_str = input('Enter a string for manual count: ')
counter = 0
for s in manual_str:
    print(manual_str[counter], end='')
    counter += 1
print('\nNumber of characters:', counter)

print("\nSub string insertion at position")
# Insert substring at particular position
base_str = input('Enter base string: ')
sub_str = input('Enter sub string: ')
ins_pos = int(input('Enter insertion position number: '))
# zero-based index adjustments
idx = ins_pos - 1
res_list = []
for i in range(idx):
    if i < len(base_str):
        res_list.append(base_str[i])
for char in sub_str:
    res_list.append(char)
for i in range(idx, len(base_str)):
    res_list.append(base_str[i])
final_str = ''.join(res_list)
print("Result string:", final_str)
