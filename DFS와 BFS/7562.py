import sys
from collections import deque
def bfs(start:list, end:list):
    dx = [2, 2, 1, -1, -2, -2, -1, 1]
    dy = [-1, 1, 2, 2, 1, -1, -2, -2]
    q = deque()
    q.append(start)
    while q:
        y, x = q.popleft()
        if y == end[0] and x == end[1]:
            return matrix[y][x]
        for p in range(8):
            yy = y + dy[p]
            xx = x + dx[p]
            if 0 <= xx < l and 0 <= yy < l:
                if matrix[yy][xx] == 0:
                    matrix[yy][xx] = matrix[y][x] + 1
                    q.append([yy, xx])
    return -1


ans_arr = []
# 입력 부분은 아래와 같다.
case = int(sys.stdin.readline())
for _ in range(case):
    l = int(sys.stdin.readline())
    # l = 체스판의 크기를 의미한다.
    matrix = [[0 for col in range(l)]for row in range(l)]
    # 체스판 배열을 선언한다. 각 성분은 0으로 초기화 되어 있다.
    start_point = list(map(int, sys.stdin.readline().split()))
    end_point = list(map(int, sys.stdin.readline().split()))
    matrix[start_point[1]][start_point[0]] = 0
    ans_arr.append(bfs(start_point, end_point))
    
print(*ans_arr,sep='\n')
    