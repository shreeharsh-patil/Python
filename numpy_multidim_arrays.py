import numpy as np

print("2D Array basics")
arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Full 2D array:")
print(arr_2d)
print("2nd element of 1st row (index [0,1]):", arr_2d[0, 1])

print("\nCreate 2D arrays using zeros()")
zeros_2d = np.zeros((3, 4), int)
print(zeros_2d)

print("\nCreate 2D arrays using ones()")
ones_2d = np.ones((3, 4), float)
print(ones_2d)

print("\nRetrieve and display nested list elements using for loops")
grid_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Row by row:")
for row in grid_data:
    print(row)
print("All flattened element access:")
for row in grid_data:
    for val in row:
        print(val, end=' ')
print()

print("\nRetrieve elements from a 3D structure using nested for loops")
cube_data = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
]
for group in cube_data:
    for row in group:
        for val in row:
            print(val, end='\t')
        print()
    print()

print("Perform slicing/reshaping operations on arrays")
base_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
reshaped = np.reshape(base_matrix, (3, 3))
print("Reshaped matrix:\n", reshaped)
print("Full slices examples [:, :] and [:] produce original views:")
print(reshaped[:, :])
