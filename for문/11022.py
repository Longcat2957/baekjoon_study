# 빠른 A+B
import sys
input_T = sys.stdin.readline()
result = []
num1_list = []
for c in range(int(input_T)):
    num1, num2 = map(int, sys.stdin.readline().split())
    result.append(num1+num2)
    num1_list.append(num1)
for c in range(int(input_T)):
    print(f'Case #{c+1}: {num1_list[c]} + {result[c] - num1_list[c]} = {result[c]}')