import sys
N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
left, right = 0, 0
s = nums[0]
# s = 부분합을 의미한다.
length = 100001
# 초기값, 최대길이를 의미합니다.

while True:
    if s >= S:
        # 부분합이 S 값보다 크거나 같은 경우
        s -= nums[left]
        # 왼쪽 숫자를 뺀다,
        length = min(length, right - left + 1)
        left += 1
    else:
        right += 1
        if right == N:
            break
            # right가 리스트의 범위를 초과했을 경우 while문 종료
        s += nums[right]
        # right가 1증가하면서 s에 값을 추가한다.

if length == 100001:
    print(0)
else:
    print(length)