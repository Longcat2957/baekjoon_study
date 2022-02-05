import sys
input = sys.stdin.readline

M = int(input())
# M은 수행해야 하는 연산의 수 이다.
data_set = [0 for __ in range(21)]

for _ in range(M):
    string = input().strip()
    if string[:3] == 'add':
        op, num = string.split()
        if data_set[int(num)] == 0:
            data_set[int(num)] = 1
    elif string[:6] == 'remove':
        op, num = string.split()
        if data_set[int(num)] == 1:
            data_set[int(num)] = 0
    elif string[:5] == 'check':
        op, num = string.split()
        if data_set[int(num)] == 1:
            print(1)
        elif data_set[int(num)] == 0:
            print(0)
    elif string[:6] == 'toggle':
        op, num = string.split()
        if data_set[int(num)] == 1:
            data_set[int(num)] = 0
        elif data_set[int(num)] == 0:
            data_set[int(num)] = 1
    elif string[:3] == 'all':
        for i in range(21):
            data_set[i] = 1
    elif string[:5] == 'empty':
        for i in range(21):
            data_set[i] = 0


