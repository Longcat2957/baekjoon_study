import sys
K, N = map(int, input().split())
num_list = []
for i in range(K):
    str = sys.stdin.readline().strip()
    num = int(str)
    num_list.append(num)

start = 1
end = max(num_list)
while start <= end:
    mid = (start + end) // 2
    lines = 0
    for num in num_list:
        lines += num // mid
    
    if lines >= N:
        start = mid +1
    else:
        end = mid -1

print(end)