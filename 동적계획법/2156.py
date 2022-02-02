import sys
input = sys.stdin.readline
n = int(input())
# n 포도주 잔의 개수 이다.
wine_list = [0]
matrix = [[0,0] for col in range(n)]
for i in range(n):
    push = int(input())
    if i == 0:
        matrix[i][0] = push
    elif i == 1:
        matrix[i][0] = push + matrix[i-1][1]
        matrix[i][1] = push + matrix[i-1][0]
    elif i == 2:
        matrix[i][0] = push + matrix[i-2][0]
        matrix[i][1] = push + matrix[i-1][0]
    elif i >= 3:
        matrix[i][0] = push + matrix[i-2][1]
        matrix[i][1] = push + matrix[i-1][0]


max_value = -1
for i in range(n):
    max_value = max(max_value, max(matrix[i]))

print(max_value)