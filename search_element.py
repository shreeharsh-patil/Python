# Searching elements in group
group1 = [1, 2, 3, 4, 5]
search = int(input("enter the element to be searched: "))
for element in group1:
    if search == element:
        print('Element found in group')
        break
else:
    print('Element not found in group')
