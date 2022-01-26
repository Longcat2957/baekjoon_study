import sys
N = int(sys.stdin.readline())
all_list = []
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    all_list.append([start, end])

all_list.sort(key = lambda x : (x[1], x[0]))
# 빨리 끝나는 순서대로 정렬한다.
# 다음으로는 빨리 시작하는 순서대로 정렬한다.
ans_list = []
for i in range(N):
    if i == 0:
        ans_list.append(all_list[i])
    else:
        if ans_list[-1][1] > all_list[i][0]:
            continue
        elif ans_list[-1][1] <= all_list[i][0]:
            ans_list.append(all_list[i])

print(len(ans_list))