import sys
string_in = sys.stdin.readline().split('-')
num_list = []
for i in string_in:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num_list.append(cnt)

ans = num_list[0]
for i in range(1, len(num_list)):
    ans -= num_list[i]
print(ans)