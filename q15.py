N = int(input("Enter a positive integer N: "))

sum_squares = sum(i ** 2 for i in range(1, N + 1))
print("Sum of squares:", sum_squares)