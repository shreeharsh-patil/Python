# WAP to display prime numbers
max_val = int(input('Upto what number? : '))
for num in range(2, max_val + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
