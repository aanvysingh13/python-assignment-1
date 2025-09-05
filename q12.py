a = float(input("Enter the first side length: "))
b = float(input("Enter the second side length: "))
c = float(input("Enter the third side length: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Yes, the lengths can form a triangle.")
else:
    print("No, the lengths cannot form a triangle.")
