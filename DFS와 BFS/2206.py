import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]
dist = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]

for n in range(N):
    matrix[n] = list(map(int, sys.stdin.readline().strip()))
def bfs():
    q = deque()
    q.append([0,0,0])
    dist[0][0][0] = 1
    while q:
        y, x, c = q.popleft()
        if y == N-1 and x == M-1:
            return dist[y][x][c]
        for p in range(4):
            yy = y + dy[p]
            xx = x + dx[p]
            
            if 0 <= xx < M and 0 <= yy < N:
                if matrix[yy][xx] == 0 and dist[yy][xx][c] == 0:
                    q.append([yy, xx, c])
                    dist[yy][xx][c] = dist[y][x][c] + 1

                elif matrix[yy][xx] == 1 and c == 0:
                    q.append([yy, xx, c+1])
                    dist[yy][xx][c + 1] = dist[y][x][c] + 1
                    
    return -1

print(bfs())
