import sys
from collections import deque
# bfs 구현을 위해 데크를 임포트 한다.
input = sys.stdin.readline
v = int(input())

board = [[] for _ in range(v+1)]

for _ in range(v):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-1, 2):
        board[temp[0]].append((temp[i], temp[i+1]))
        # temp[0]은 시작점, 짝수번째는 도착점, 홀수번째는 가중치이다.


def bfs(idx):
    visited = [-1] * (v+1)
    # 방문 여부를 -1로 초기화 한다.
    q = deque()
    q.append(idx)
    # 시작점을 큐에 푸쉬한다.
    visited[idx] = 0
    # 시작점을 방문했으므로 방문 여부를 0으로 세트한다.(-1 : 완전 미방문)

    max_value = [0, 0]

    while q:
        old = q.popleft()
        # 큐에서 가장 앞에 있는 값을 꺼낸다.
        for new in board[old]:
            # 시작점으로 부터 연결된 모든 후속 도착점에 대하여
            if visited[new[0]] == -1: 
                # 방문한 적이 없을때 다음의 연산을 수행한다.
                visited[new[0]] = visited[old] + new[1]
                # 현재까지의 가중치 합에 새롭게 추가되는 가중치를 더한다.
                q.append(new[0])
                # 다음 도착점을 큐에 저장함으로써 다음 방문을 예약한다.
                if max_value[0] < visited[new[0]]:
                    # 새롭게 가중치를 계산한 값으로 부터 기존의 잠재적인 정답보다 더 큰 값을 가진다면
                    max_value[0] = visited[new[0]]
                    max_value[1] = new[0]
                    # 값을 새롭게 갱신한다.
                    # 첫 번째는 가중치의 합이고 두 번째는 node의 인덱스이다.

    return max_value

value, node = bfs(1)
answer, node2 = bfs(node)
# 트리에서 지름이란, 가장 먼 두 정점 사이의 거리 혹은 가장 먼 두 정점을 연결하는 경로를 의미한다.
# 선형 시간안에 트리에서 지름을 구하는 방법은 다음과 같다.
# 1. 트리에서 임의의 정점 x를 잡는다.
# 2. 정점 x에서 가장 먼 정점 y를 찾는다.
# 3. 정점 y에서 가장 먼 정점 z를 찾는다.
# 트리의 지름은 정점 y와 정점 z를 연결하는 경로다.
print(answer)