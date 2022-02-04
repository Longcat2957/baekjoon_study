import sys
import heapq

input = sys.stdin.readline

N = int(input())
# 백준이가 외치는 정수의 개수
# 1보다 크거나 갈고, 100,000보다 작거나 같다.
left_arr = []
# 왼쪽 힙에는 중간 값보다 더 작은 값이 들어간다.
right_arr = []
# 오른 힙에는 중간 값보다 더 큰 값이 들어간다.
answers = []
for i in range(N):
    num = int(input())
    
    if len(left_arr) == len(right_arr):
        heapq.heappush(left_arr, (-num, num))
        # 파이썬은 최소 힙을 기본으로 하고 있으므로 마이너스 부호를 통해 최대 힙으로 저장한다.
    else:
        # len(left_arr) != len(right_arr):
        heapq.heappush(right_arr, (num, num))
        # 오른 힙에는 최소 힙으로 저정한다.
    
    if right_arr and left_arr[0][1] > right_arr[0][0]:
        # 오른쪽 힙이 비어있지 않으면서
        # 오른쪽 힙의 최소값이 왼쪽 힙의 최대값보다 작은 경우
        # 문제의 초기 조건에 모순이므로 다음과 같이 값을 전환한다.
        max = heapq.heappop(left_arr)[1]
        min = heapq.heappop(right_arr)[0]
        heapq.heappush(left_arr, (-min, min))
        heapq.heappush(right_arr, (max, max))
        # 값을 꺼내어(pop) 서로 위치를 바꿔서 푸쉬한다.
    
    answers.append(left_arr[0][1])
    # 따라서 중간 값은 반드시 왼쪽 힙의 최 상단에 위치하게 된다.

print(*answers, sep='\n')