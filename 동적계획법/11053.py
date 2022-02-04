import sys
input = sys.stdin.readline

size_of_arr = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(size_of_arr)]
for i in range(size_of_arr):
    # 배열의 원소에 대해서
    for j in range(i):
        # 위에서 택한 배열의 원소보다 작은 인덱스를 가진 원소들에 대해서
        if arr[i] > arr[j] and dp[i] < dp[j]:
            # 이전의 원소보다 더 크면서 가장 큰 길이에 대하여
            dp[i] = dp[j]
            # 가장 큰 길이를 할당하고
    dp[i] += 1
    # 길이가 1 증가했다.
print(max(dp))
# dp에서의 가장 큰 값을 출력한다.
