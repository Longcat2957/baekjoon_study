import math
a = int(input())
num1 = round(math.pi * (a**2), 6)
num2 = round(float(2 * (a**2)), 6)
print(f"{num1:.6f}")
print(f"{num2:.6f}")