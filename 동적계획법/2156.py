import sys
input = sys.stdin.readline
n = int(input())
# n 포도주 잔의 개수 이다.
wines = [0]
for _ in range(n):
    wines.append(int(input()))
matrix = [ 0 for col in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        matrix[i] = wines[1]
    elif i == 2:
        matrix[i] = wines[1] + wines[2]
    elif i >= 3:
        matrix[i] = max(matrix[i-1], matrix[i-3] + wines[i-1] + wines[i], matrix[i-2] + wines[i])

print(matrix[n])