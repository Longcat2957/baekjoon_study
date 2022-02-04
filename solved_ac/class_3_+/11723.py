import sys
input = sys.stdin.readline

M = int(input())
# M은 수행해야 하는 연산의 수 이다.
data_set = set()
answers = []
for _ in range(M):
    string = input().strip()
    if string[:3] == 'add':
        op, num = string.split()
        data_set.add(int(num))
    elif string[:6] == 'remove':
        op, num = string.split()
        if int(num) in data_set:
            data_set.remove(int(num))
    elif string[:5] == 'check':
        op, num = string.split()
        if int(num) in data_set:
            answers.append(1)
        elif int(num) not in data_set:
            answers.append(0)
    elif string[:6] == 'toggle':
        op, num = string.split()
        if int(num) in data_set:
            data_set.remove(int(num))
        elif int(num) not in data_set:
            data_set.add(int(num))
    elif string[:3] == 'all':
        data_set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif string[:5] == 'empty':
        data_set = set()

print(*answers,sep='\n')
