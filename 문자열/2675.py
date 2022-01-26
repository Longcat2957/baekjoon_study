T = int(input())
empty_list = []
while True:
    try:
        cnt, word = input().split()
        empty_list.append([int(cnt), word])
    except:
        break
for c in range(T):
    for i in range(len(empty_list[c][1])):
        print(empty_list[c][0]*empty_list[c][1][i], end='')
    print('\n',end='')