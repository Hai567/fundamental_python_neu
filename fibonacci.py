f1 = 1
f2 = 1

user = int(input("Enter the number you want to find the Fibonacci sequence of: "))
if user > 2:
    for i in range(2, user):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    print(f3)
else:
    print("1")