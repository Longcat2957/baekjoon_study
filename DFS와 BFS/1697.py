from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
dist = [0 for _ in range(100001)]
q = deque([N])
def BFS():
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            break
        for xx in (x-1, x+1, 2*x):
            if 0 <= xx < 100001 and dist[xx] == 0:
                # dist[xx] 가 0이 아닌 값을 가지고 있다면 이미 한번 방문한 적이 있다는 의미이다.
                dist[xx] = dist[x] + 1
                q.append(xx)

BFS()
