# Factorial recursion example
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Recursion: Factorial calculation 1 to 10")
for i in range(1, 11):
    print('Factorial of {} is {}'.format(i, factorial(i)))

print("\nPrime verification function")
def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

p_num = int(input('Enter a number to test primality: '))
if is_prime(p_num) == 1:
    print(p_num, 'is prime')
else:
    print(p_num, 'is not prime')

print("\nMulti-return results (Sum, Sub, Mul, Div)")
def calc_operations(a, b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b if b != 0 else 0
    return c, d, e, f

res = calc_operations(20, 5)
print('Operation results for 20,5:', res)

print("\nPositional and Keyword arguments")
def attach(s1, s2):
    s3 = s1 + s2
    print('Concatenated string:', s3)

attach('Shreeharsh', 'Patil')  # positional

def grocery_list(item, price):
    print('Item = %s, Price = %.2f' % (item, price))

grocery_list(item='Salt', price=19.75)  # keyword
grocery_list(price=108.00, item='oil')  # keyword

print("\nDefault arguments usage")
def grocery_def(item, price=40.00):
    print('Item = %s, Price = %.2f' % (item, price))

grocery_def(item='Salt', price=50.75)  # explicit
grocery_def(item='Sugar')  # fallback default

print("\nVariable length arguments (*args)")
def add_nums(farg, *args):
    print('Formal argument =', farg)
    sum_args = sum(args)
    print('Total sum (farg + *args) =', (farg + sum_args))

add_nums(5, 10)
add_nums(5, 10, 20, 30)

print("\nKeyword variable arguments (**kwargs)")
def display_kwargs(farg, **kwargs):
    print('Formal argument =', farg)
    for key, val in kwargs.items():
        print('key={}, value={}'.format(key, val))

display_kwargs(5, rno=66)
display_kwargs(5, rno=66, name='Shreeharsh')

print("\nAverage computation helper")
def calculate_avg(lst):
    length = len(lst)
    if length == 0:
        return 0, 0
    total = sum(lst)
    avg = total / length
    return total, avg

input_vals = input('Enter numbers separated by space for average: ')
num_arr = [int(x) for x in input_vals.split()]
if num_arr:
    tot_res, avg_res = calculate_avg(num_arr)
    print('Total:', tot_res)
    print('Average:', avg_res)

print("\nTower of Hanoi solving (recursion)")
def solve_towers(n, source, destination, intermediate):
    if n == 1:
        print('Move disk 1 from pole %s to pole %s' % (source, destination))
    else:
        # move n-1 disks to intermediate
        solve_towers(n - 1, source, intermediate, destination)
        # move nth disk to destination
        print('Move disk %i from pole %s to pole %s' % (n, source, destination))
        # move n-1 disks from intermediate to destination
        solve_towers(n - 1, intermediate, destination, source)

h_disks = int(input('Enter number of disks for Tower of Hanoi: '))
if h_disks > 0:
    solve_towers(h_disks, 'A', 'C', 'B')
