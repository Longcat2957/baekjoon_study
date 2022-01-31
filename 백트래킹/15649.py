import sys
N, M = map(int, sys.stdin.readline().split())
stack = []

def dfs():
    if len(stack) == M:
        # 백트래킹 제약조건 = Length is M
        print(' '.join(map(str,stack)))
    for i in range(1, N+1):
        if i not in stack:
            stack.append(i)
            dfs()
            # 재귀를 통해 dfs를 구현한다.
            stack.pop()

dfs()