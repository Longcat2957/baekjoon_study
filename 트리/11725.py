import sys

input = sys.stdin.readline
num_of_node = int(input())
# 노드의 개수는 위와 같다.(N)

tree = [[]for _ in range(num_of_node + 1)]
list_of_points = [0 for _ in range(num_of_node + 1)]

for _ in range(num_of_node - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(start:int):
    # DFS(깊이 우선 탐색)
    visited = []
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in tree[v]:
                if list_of_points[w] == 0:
                    list_of_points[w] = v
                    stack.append(w)

DFS(1)

for i in range(2, num_of_node + 1):
    print(list_of_points[i])