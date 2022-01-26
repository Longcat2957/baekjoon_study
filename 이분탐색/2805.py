import sys
n, m = map(int, sys.stdin.readline().split())
dataset = list(map(int, sys.stdin.readline().split()))
left, right = 1, max(dataset)

while left <= right:
    mid = (left+right)//2
    sum = 0
    for tree in dataset:
        if tree >= mid:
            sum += tree - mid
    
    if sum >= m:
        left = mid + 1
    else:
        right = mid -1
print(right)