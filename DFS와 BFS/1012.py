import sys
sys.setrecursionlimit(99999)
T = int(sys.stdin.readline())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(x, y):
    for p in range(4):
        xx = x + dx[p]
        yy = y + dy[p]
        if 0 <= xx < M and 0 <= yy < N and arr[yy][xx] == 1:
            arr[yy][xx] = 0
            BFS(xx, yy)

answer_list = []
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    for i in range(M):
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                BFS(i, j)
    answer_list.append(cnt)

for i in range(T):
    print(answer_list[i])