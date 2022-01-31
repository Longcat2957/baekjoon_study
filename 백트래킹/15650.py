import sys
# 백트래킹은 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기해
# 정답을 찾아가는 범용적인 알고리즘으로 제약 충족 문제에 특히 유용하다.
# DFS는 백트래킹의 골격을 이루는 일고리즘이다.

# DFS 수도코드(stack 이용)
# DFS-iterative(G, v)
#     let S be a stack
#     S.push(v)
#     while S is not empty do
#         v = S.pop()
#         if v is not labeled as discovered then
#             label v as discovered
#             for all edges from v to w in G.adjacentEdges(v) do
#                 S.push(w)

# DFS 파이썬 코드
# def iterative_dfs(start_v):
#     discovered = []
#     stack = [start_v]
#     while stack:
#         v = stack.pop()
#         if v not in discovered:
#             discovered.append(v)
#             for w in graph[v]:
#                 stack.append(w)
#     return discovered

N, M = map(int, sys.stdin.readline().split())
# 1, 2, 3, .... N-1, N
# M개의 숫자를 중복 없이 고른다.

def DFS():
    visited = []
    stack = [1]
    while stack:
        if len(visited) == M:
            print(*visited, sep=' ')
            visited.pop()
        v = stack.pop()
        if v not in visited and v <= N:
            visited.append(v)
            stack.append(v+1)
        elif v > N and len(visited) > 0:
            stack.append(visited.pop() + 1)
        else:
            break


DFS()