from re import L
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
arr = []

for _ in range(N):
    num = int(input())
    arr.append(num)

arr.sort()

left = 1
# 임의의 두 집 사이의 최소 길이
right = arr[-1] - arr[0]
# 임의의 두 집 사이의 최대 길이

result = 0

while left <= right:
    mid = left + (right - left)//2
    # i-1, i-2 번째 설치된 공유기 사이의 거리를 갱신
    ex = arr[0]
    count = 1
    
    for i in range(1, len(arr)):
        # arr[0]은 첫 번째로 공유기가 설치되므로 제외할 것
        if arr[i] >= ex + mid:
            count += 1
            ex = arr[i]
    
    if count >= C:
        # 마지막 순간에 도달하는 경우(모든 공유기 소모)
        left = mid + 1
        result = mid
    else:
        right = mid - 1
        
print(result)