import sys
from collections import deque
N = int(sys.stdin.readline())


def promising(i, col):
    for k in range(1, i):
        if (col[i] == col[k]) or (abs(col[i] - col[k]) == i - k):
            return False
    return True

def solution(n):
    answer = 0
    stack = deque([[0 for _ in range(n+1)]])
    while stack:
        v = stack.pop()
        if v[0] == n:
            answer += 1
            continue
        v[0] += 1
        i = v[0]
        for j in range(1, n+1):
            v[i] = j
            vv = v[:]
            if promising(i, vv):
                # if promising(i, v) == True, 조건을 만족하는 경우
                stack.append(vv)
    print(answer)
        

solution(N)