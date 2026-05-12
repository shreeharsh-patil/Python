# WAP to display Fibonacci number
n = int(input('How many numbers do you want in series? : '))
f1 = 0
f2 = 1
c = 2

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print(f1)
elif n == 2:
    print(f1)
    print(f2)
else:
    print(f1)
    print(f2)
    while c < n:
        f = f1 + f2
        print(f)
        f1, f2 = f2, f
        c += 1
