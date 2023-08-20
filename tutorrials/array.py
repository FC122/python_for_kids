n = int(input("Enter the length of the array: "))
a = []

for i in range(n):
    num = int(input("Enter an element: "))
    a.append(num)

for i in range(n - 1):
    if a[i] > a[i + 1]:
        print(a[i])
