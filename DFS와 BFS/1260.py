import sys
N, M, V = map(int, input().split())
visited = [False * i for i in range(N+1)]
print(visited)
graph = [[]* i for i in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if b not in graph[a]:
        graph[a].append(b)
        graph[a].sort()
    if a not in graph[b]:
        graph[b].append(a)
        graph[b].sort()
# 정점의 개수 N(1<= N <= 1000)
# 간선의 개수 M(1<= M <= 10000)
# 정점의 번호 V
print(graph)
# DFS(깊이 우선 탐색)
# 일반적으로 DFS는 스택으로 구현하며, 재귀를 이용하면 더 간단하게 구현할 수 있다.
# 다음은 재귀를 이용한 구현 방식이다.
ans_1 = []
def DFS(graph:list, v:int):
    ans_1.append(v)
    visited[v] = True
    if len(graph[v]) == 0 or len(ans_1) == N:
        return
    # 더이상 전개할 수 없을 경우 종료한다.
    elif len(graph[v]) > 0:
        for vertex in graph[v]:
            if len(ans_1) != N and visited[vertex] == False:
                DFS(graph, vertex)

DFS(graph, V)
print(ans_1)