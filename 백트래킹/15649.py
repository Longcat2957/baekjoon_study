import sys
N, M = map(int, sys.stdin.readline().split())
stack = []

def dfs():
    if len(stack) == M:
        print(' '.join(map(str,stack)))
    for i in range(1, N+1):
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()

dfs()