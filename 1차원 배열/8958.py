import sys
def sigma(int):
    return ((int)*(int+1))/2
n = int(sys.stdin.readline())
empty_list = []
for i in range(n):
    empty_list.append(sys.stdin.readline().strip()+'X')
for i in range(n):
    result, counter = 0, 0
    for c in range(len(empty_list[i])):
        if empty_list[i][c] == 'O':
            counter += 1
        elif empty_list[i][c] == 'X':
            result += sigma(counter)
            counter = 0
    print(int(result))