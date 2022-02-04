import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
# N = 정점의 개수, M = 간선의 개수

graph = [[]for row in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS로 풀이 할 수 있도록 한다.

def dfs(start:int):
    global visited
    stack = [start]
    while stack:
        v = stack.pop()
        if visited[v] != True:
            visited[v] = True
            for next in graph[v]:
                stack.append(next)
count = 0
for j in range(1, N+1):
    if not visited[j]:
        dfs(j)
        count += 1
        

print(count)