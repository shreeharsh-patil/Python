from numpy import *

print("1D character array using array()")
arr1 = array(['a', 'b', 'c', 'd'])
print(arr1)

print("\nRetrieving elements using indexing")
arr2 = array(['Canacona', 'Panjim', 'Margao', 'Quepem', 'Verna'])
print(arr2)

print("\nArray using linspace()")
arr_lin = linspace(0, 15, 5)
print('a =', arr_lin)

print("\nArray using logspace()")
arr_log = logspace(1, 6, 4)
for i in range(len(arr_log)):
    print('%.1f' % arr_log[i], end=' ')
print()

print("\nArray using arange() for evens")
arr_ar = arange(2, 17, 2)
print(arr_ar)

print("\nArray using zeros() and ones()")
arr_z = zeros(7, int)
print("Zeros:", arr_z)
arr_o = ones(7)
print("Ones:", arr_o)

print("\nMathematical operations on numpy array")
op_arr = array([1, -2, 3, 4, 5])
print("Original array:", op_arr)
print("After adding 5:", op_arr + 5)
print("After subtracting 5:", op_arr - 5)
print("After multiplying by 5:", op_arr * 5)
print("After dividing by 5:", op_arr / 5)
print("After modulus 5:", op_arr % 5)
print("Expression value (x+5)**2 - 10:", (op_arr + 5) ** 2 - 10)
print("Sin values:", sin(op_arr))
print("Cos values:", cos(op_arr))
print("Tan values:", tan(op_arr))
print("Max element:", op_arr.max())
print("Min element:", op_arr.min())
print("Sum of elements:", op_arr.sum())
print("Mean of elements:", op_arr.mean())

print("\nLogical functions on arrays")
a = array([1, 2, 3], int)
b = array([4, 5, 6], int)
print("logical_and (a>0, a<4):", logical_and(a > 0, a < 4))
print("logical_or (b>=0, b==1):", logical_or(b >= 0, b == 1))
print("logical_not (b):", logical_not(b))

print("\nCompare arrays with 'where'")
a_comp = array([10, 20, 30, 40, 50], int)
b_comp = array([1, 21, 3, 40, 51], int)
# if a_comp > b_comp then take element from a_comp, else from b_comp
c_res = where(a_comp > b_comp, a_comp, b_comp)
print(c_res)

print("\nArray view of existing array")
a_view = arange(4, 17)
b_view = a_view.view()
print('Original:', a_view)
print('New View:', b_view)
b_view[0] = 99
print('After modifying view[0]:')
print('Original:', a_view)
print('New View:', b_view)

print("\nArray slicing operations")
slice_arr = arange(1, 10)
print("Full array:", slice_arr)
print("Slices [1:6:2]:", slice_arr[1:6:2])
print("Full view [::]:", slice_arr[::])
print("Reverse slice [-2:2:-1]:", slice_arr[-2:2:-1])
print("Truncated [:-2:]:", slice_arr[:-2:])

print("\nStep-slicing access with while loop")
iter_arr = arange(1, 15)
slice_res = iter_arr[1:6:2]
print("Sample sliced array:", slice_res)
i = 0
while i < len(slice_res):
    print(slice_res[i])
    i += 1
