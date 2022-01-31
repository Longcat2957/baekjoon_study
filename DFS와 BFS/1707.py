import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
T = int(sys.stdin.readline())
# T = 테스트 케이스의 수


def dfs(v, type:int):
    visited[v] = type
    # 방문한 노드에 1을 할당
    for j in graph[v]:
        if visited[j] == 0:
            if not dfs(j, -type):
                return False
        elif visited[j] == visited[v]:
            return False
    return True
            
ans_list = []

for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for row in range(V+1)]
    visited = [0] * (V+1)
    for e in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    result = True
    for i in range(1, V+1):
        if visited[i] == 0:
            result = dfs(i, 1)
            if not result:
                break
    # 케이스 종료 후
    if result:
        ans_list.append('YES')
    else:
        ans_list.append('NO')
    
print(*ans_list,sep='\n')