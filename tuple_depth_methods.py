# Program to accept elements in form of tuple and perform mathematical ops
user_str = input('Enter numbers separated by spaces for tuple sum: ')
raw_lst = [int(x) for x in user_str.split()]
num_tup = tuple(raw_lst)
print("Created tuple:", num_tup)
print("Sum of elements:", sum(num_tup))
if len(num_tup) > 0:
    print("Average:", sum(num_tup) / len(num_tup))

print("\nFinding occurrences and indices")
t1 = (10, 20, 30, 40, 50, 20, 10)
print("Tuple t1:", t1)
try:
    idx = t1.index(30)
    print("Index of element 30:", idx)
except ValueError:
    print("Element not in tuple")
print("Occurrence count of 10:", t1.count(10))

print("\nSorting a tuple of strings")
names_tup = ('Shreeharsh', 'Ajay', 'Rohit', 'Omkar')
print('Original tuple:', names_tup)
# convert to list then sort
temp_sorted_list = sorted(names_tup)
sorted_tup = tuple(temp_sorted_list)
print('Sorted tuple:', sorted_tup)

print("\nModifying tuple contents via intermediate list (Insertion example)")
base_tuple = (10, 20, 30, 40, 50)
print('Original:', base_tuple)
cast_list = list(base_tuple)
try:
    ins_idx = int(input('Enter insertion index for base tuple: '))
    ins_val = int(input('Enter element value to insert: '))
    cast_list.insert(ins_idx, ins_val)
    final_tup = tuple(cast_list)
    print('Resulting tuple:', final_tup)
except ValueError as e:
    print("Invalid numerical input.", e)

print("\nNested tuple iteration")
multi_tup = ( (1, 2, 3), (4, 5, 6) )
print('Retrieving specific item (0,1):', multi_tup[0][1])
print('Iterating elements:')
for row in multi_tup:
    for val in row:
        print(val, end=' ')
    print()

print("\nTuple slicing mechanisms")
slice_tup = (1, 2, 3, 4, 5, 6)
print('Slicing indices [1:4]:', slice_tup[1:4])
print('Steps [0:6:2]:', slice_tup[0:6:2])
print('Reverse traversal [::-1]:', slice_tup[::-1])
