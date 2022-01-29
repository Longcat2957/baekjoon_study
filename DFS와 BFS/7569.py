import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
matrix = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
queue = deque([])
for h in range(H):
    for n in range(N):
        matrix[h][n] = list(map(int, sys.stdin.readline().split()))
        for m in range(M):
            if matrix[h][n][m] == 1:
                queue.append([h, n, m])
dx, dy, dz = [1, 0, -1, 0, 0, 0], [0, 1, 0, -1, 0, 0], [0, 0, 0, 0, 1, -1]
def BFS():
    while queue:
        z, y, x = queue.popleft()
        for p in range(6):
            zz = z + dz[p]
            yy = y + dy[p]
            xx = x + dx[p]
            if 0 <= xx < M and 0 <= yy < N and 0 <= zz < H and matrix[zz][yy][xx] == 0:
                queue.append([zz, yy, xx])
                matrix[zz][yy][xx] = matrix[z][y][x] + 1

BFS()
ans = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if matrix[h][n][m] == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(matrix[h][n]))

print(ans-1)