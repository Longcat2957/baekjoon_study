import sys
N, M = map(int, sys.stdin.readline().split())
stack = []
def DFS():
    if len(stack) == M:
        print(*stack, sep=' ')
        return
    
    for i in range(1, N+1):
        stack.append(i)
        DFS()
        stack.pop()
DFS()