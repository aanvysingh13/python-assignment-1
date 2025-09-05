P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interest: "))
T = int(input("Enter Time (in years): "))

A = P * ((1 + R / 100) ** T)
CI = A - P

print("Compound Interest:", CI)