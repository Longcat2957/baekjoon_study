import queue
import sys
N, M, V = map(int, input().split())
graph = [[]* i for i in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort(reverse=True)
# 정점의 개수 N(1<= N <= 1000)
# 간선의 개수 M(1<= M <= 10000)
# 정점의 번호 V
# DFS(깊이 우선 탐색)
# 일반적으로 DFS는 스택으로 구현하며, 재귀를 이용하면 더 간단하게 구현할 수 있다.
# 다음은 재귀를 이용한 구현 방식이다.
ans_dfs = []
ans_bfs = []
def DFS(graph:list, v:int):
    visited = []
    stack = [v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            print(v, end = ' ')
            for w in graph[v]:
                stack.append(w)
    return visited

def BFS(graph:list, v:int):
    print(v,end=' ')
    visited = [v]
    from collections import deque
    queue = [v]
    while queue:
        v = queue.pop(0)
        for w in reversed(graph[v]):
            if w not in visited:
                visited.append(w)
                print(w,end = ' ')
                queue.append(w)
    return visited

DFS(graph, V)
print()
BFS(graph, V)