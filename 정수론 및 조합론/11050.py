from math import factorial
N, K = map(int, input().split())
num1, num2, num3 = factorial(N), factorial(K), factorial(N-K)
result = (num1)//(num2 * num3)
print(result)