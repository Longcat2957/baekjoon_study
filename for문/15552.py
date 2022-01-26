# 빠른 A+B
import sys
input_T = sys.stdin.readline()
result = []
for c in range(int(input_T)):
    num1, num2 = map(int, sys.stdin.readline().split())
    result.append(num1+num2)
for c in range(int(input_T)):
    print(result[c])