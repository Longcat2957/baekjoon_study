import sys
input = sys.stdin.readline
num_of_cable = int(input())
arr = []
for _ in range(num_of_cable):
    n, m = map(int, input().split())
    arr.append([n,m])

arr.sort(key = lambda x:x[0])
# 왼쪽 전봇대를 기준으로 순서대로 정렬한다. 
# 이제 오른쪽 전봇대로 부터 가장 긴 증가하는 부분 수열을 구한다.

dp = [0 for _ in range(num_of_cable)]
for i in range(num_of_cable):
    # 배열의 원소에 대해서
    for j in range(i):
        if arr[i][1] > arr[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(num_of_cable - max(dp))