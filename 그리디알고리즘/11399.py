import sys
N = int(sys.stdin.readline())
time_list = list(map(int, sys.stdin.readline().split()))
time_list.sort()
sum = 0
for i in range(N):
    sum += (N-i) * time_list[i]

print(sum)