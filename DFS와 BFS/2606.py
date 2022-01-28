import sys
N = int(sys.stdin.readline())
# N = 컴퓨터의 숫자
graph = [[]*i for i in range(N+1)]
M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort()

def DFS(v:int):
    visited = []
    stack = [v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited

print(len(DFS(1)) - 1)
