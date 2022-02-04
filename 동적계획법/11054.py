import sys
input = sys.stdin.readline
size_of_arr = int(input())
arr = list(map(int, input().split()))
dp_1 = [0 for _ in range(size_of_arr)]
arr_r = arr[::-1]
dp_2 = [0 for _ in range(size_of_arr)]

for i in range(size_of_arr):
    for j in range(i):
        if arr[i] > arr[j] and dp_1[i] < dp_1[j]:
            dp_1[i] = dp_1[j]
    dp_1[i] += 1
    
for i in range(size_of_arr):
    for j in range(i):
        if arr_r[i] > arr_r[j] and dp_2[i] < dp_2[j]:
            dp_2[i] = dp_2[j]
    dp_2[i] += 1
dp_2 = dp_2[::-1]
dp_3 = []
for i in range(size_of_arr):
    dp_3.append(dp_1[i] + dp_2[i])

print(max(dp_3) - 1)