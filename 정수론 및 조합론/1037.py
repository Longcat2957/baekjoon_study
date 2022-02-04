import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
if N % 2 == 1:
    # 약수의 갯수가 홀수 인 경우 (제곱수)
    print((arr[((N+1)//2)-1])**2)

elif N % 2 == 0:
    # 약수의 갯수가 짝수인 경우
    a, b = arr[N//2 - 1], arr[N//2]
    print(a*b)