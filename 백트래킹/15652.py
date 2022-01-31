import sys
N, M =map(int, sys.stdin.readline().split())

stack = []

def dfs(start:int):
    if len(stack) == M:
        print(*stack, sep=' ')
        return
    for i in range(start, N+1):
        stack.append(i)
        dfs(i)
        stack.pop()
        
dfs(1)