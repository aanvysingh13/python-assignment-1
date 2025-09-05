n = int(input("Enter a positive integer: "))

if n <= 1:
    print(n, "is NOT a Prime Number")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(n, "is NOT a Prime Number")
            break
    else:
        print(n, "is a Prime Number")