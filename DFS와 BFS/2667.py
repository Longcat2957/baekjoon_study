import sys
N = int(sys.stdin.readline())
# N = 지도의 가로, 세로 길이이다. 지도는 정사각형 모양이다.
matrix = [[0 for col in range(N)] for row in range(N)]
for i in range(N):
    string = list(map(int, sys.stdin.readline().strip()))
    matrix[i] = string

def DFS(row:int, col:int):
    visited = []
    stack = [[col, row]]
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    while stack:
        v = stack.pop()
        if v not in visited and matrix[v[0]][v[1]] == 1:
            matrix[v[0]][v[1]] = 0
            visited.append(v)
            for p in range(4):
                xx = v[1] + dx[p]
                yy = v[0] + dy[p]
                if xx < 0 or xx >= N or yy < 0 or yy >= N:
                    continue
                else:
                    if matrix[yy][xx] == 1:
                        stack.append([yy, xx])
    if len(visited) > 0:
        return len(visited)
    else:
        return 0

ans_list =[]
# 전체 DFS 발생 횟수
for i in range(N):
    for j in range(N):
        result = DFS(i, j)
        if result > 0:
            ans_list.append(result)
print(len(ans_list))
ans_list.sort()
for a in ans_list:
    print(a)