import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr_to_set = sorted(list(set(arr)))
dict = dict()
for i in range(len(arr_to_set)):
    dict[arr_to_set[i]] = i

for j in range(N):
    print(dict[arr[j]], end=' ')
