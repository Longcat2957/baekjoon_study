import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
matrix = [[0 for col in range(M)] for row in range(N)]
queue = deque()
for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])
dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
def BFS():
    while queue:
        v = queue.popleft()
        for p in range(4):
            yy = v[0] + dy[p]
            xx = v[1] + dx[p]
            if 0 <= xx < M and 0 <= yy < N and matrix[yy][xx] == 0:
                queue.append([yy, xx])
                matrix[yy][xx] = matrix[v[0]][v[1]] + 1

BFS()
ans = 0
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
    
print(ans-1)