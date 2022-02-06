import sys
input = sys.stdin.readline
length_of_arr = int(input())
arr = list(map(int, input().split()))
visited = [0]
# 기존 11053.py 코드를 참고하여 위와 같이 자료구조를 선언한다.
# 11053문제와 다른 점은 수열의 길이가 크게 증가했다는 점이다.
# 따라서 이분 탐색을 이용하여 log N 의 시간복잡도로 풀어야 한다.

for num in arr:
    if visited[-1] < num:
        # 더 큰 값을 찾게 되면
        visited.append(num)
    else:
        # 더 큰 값을 찾지 못했을 때 이분탐색
        # 이분 탐색의 범위는 현재까지 탐색한 점 이하에 대해서 탐색한다.
        left = 0
        right = len(visited)
        
        while left < right:
            mid = left + (right - left) // 2
            if visited[mid] < num:
                left = mid + 1
            else:
                right = mid
        visited[right] = num
        # visited의 마지막 값을 교체한다.

print(len(visited) - 1)