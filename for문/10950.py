T = int(input())
empty_list = []
for c in range(T):
    empty_list.append(list(map(int, input().split())))
for c in range(len(empty_list)):
    print(empty_list[c][0] + empty_list[c][1])