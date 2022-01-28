# BFS의 특징은 각 정점을 최단경로로 방문한다는 것입니다.
import sys
N, M = map(int, sys.stdin.readline().split())
matrix = [[0 for col in range(M)] for row in range(N)]
visited_matrix = [[0 for col in range(M)] for row in range(N)]
visited_matrix[0][0] = 1
for i in range(N):
    string = list(map(int, sys.stdin.readline().strip()))
    matrix[i] = string

def BFS():
    # 시작점과 종료지점이 (0,0), (N-1,M-1)으로 고정되어 있다.
    queue = [[0, 0]]
    while queue:
        v = queue.pop(0)
        if v[0] == N-1 and v[1] == M-1:
            print(visited_matrix[v[0]][v[1]])
            return
        dx, dy = [1,0,0,-1],[0,-1,1,0]
        for p in range(4):
            yy = v[0] + dy[p]
            xx = v[1] + dx[p]
            if xx < 0 or xx > M-1 or yy < 0 or yy > N-1:
                continue
            else:
                if visited_matrix[yy][xx] == 0 and matrix[yy][xx] == 1:
                    visited_matrix[yy][xx] = visited_matrix[v[0]][v[1]] + 1
                    queue.append([yy, xx])

BFS()