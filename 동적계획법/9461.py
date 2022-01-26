import sys
T = int(sys.stdin.readline())
array = [0] * 101
array[1] = 1
array[2] = 1
array[3] = 1

for i in range(4, 101):
    array[i] = array[i-3] + array[i-2]

answer_list = []
for _ in range(T):
    num = int(sys.stdin.readline())
    answer_list.append(array[num])

for i in range(T):
    print(answer_list[i])
