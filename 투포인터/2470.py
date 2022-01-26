from os import TMP_MAX
import sys
n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))

left = 0
right = n -1
criteria = abs(arr[left] + arr[right])
answer_l = 0
answer_r = n - 1

while left < right:
    tmp = arr[left] + arr[right]
    if abs(tmp) < criteria:
        # 더 작은 값이 발견되는 경우 새로운 데이터를 저장한다.
        answer_l = left
        answer_r = right
        criteria = abs(tmp)
        if criteria == 0:
            break
    
    if tmp > 0 :
        right -= 1
    elif tmp < 0:
        left += 1

print(arr[answer_l], arr[answer_r])
    