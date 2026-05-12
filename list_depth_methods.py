# 1. Creating list with some values
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("1. Initial list:", my_list)

# 2. Find the index of an element
target_find = 40
if target_find in my_list:
    print("2. Index of 40 is:", my_list.index(target_find))

# 3. Append an element to end
my_list.append(100)
print("3. After appending 100:", my_list)

# 4. Insert an element at a specified position
my_list.insert(0, 5)
print("4. After inserting 5 at start index:", my_list)

# 5. Create a separate object copy
list_clone = my_list.copy()
print("5. Cloned list:", list_clone)

# 6. Extend the list by appending another iterable
my_list.extend([110, 120])
print("6. After extending with [110, 120]:", my_list)

# 7. Count occurrences of an element
print("7. Occurrence count of 10:", my_list.count(10))

# 8. Remove first occurrence of specified element
my_list.remove(120)
print("8. After removing 120:", my_list)

# 9. Remove and return the last item
popped_val = my_list.pop()
print("9. After popping last item {}: {}".format(popped_val, my_list))

# 10. Sort items in ascending order
unsorted_data = [10, 2, 45, 1]
unsorted_data.sort()
print("10. Sorted list [10, 2, 45, 1]:", unsorted_data)

# 11. Reverse order of items
my_list.reverse()
print("11. Reversed my_list:", my_list)

# 12. Clear all elements
temp_l = [1, 2, 3]
temp_l.clear()
print("12. Cleared temp list:", temp_l)

print("\nFinding common elements between two lists")
list_x = [10, 20, 30, 40, 50]
list_y = [20, 30, 60, 70]
# list comprehension style
set_x = set(list_x)
set_y = set(list_y)
common_res = list(set_x.intersection(set_y))
print("List X:", list_x)
print("List Y:", list_y)
print("Common elements:", common_res)

print("\nNested lists syntax usage (matrix representation)")
nested_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("First row:", nested_grid[0])
print("Iterating nested rows:")
for r in nested_grid:
    print(r)

print("\nBubble Sort manual implementation")
bubble_in = input("Enter space-separated numbers for Bubble Sort: ")
b_list = [int(x) for x in bubble_in.split()]
n_b = len(b_list)
print("Before sort:", b_list)
# Outer loop for pass num
for i in range(n_b - 1):
    swapped = False
    # Inner loop for comparison, reducing range each pass
    for j in range(n_b - 1 - i):
        if b_list[j] > b_list[j + 1]:
            # swap
            b_list[j], b_list[j + 1] = b_list[j + 1], b_list[j]
            swapped = True
    if not swapped:
        break
print("Sorted list using Bubble Sort:", b_list)
