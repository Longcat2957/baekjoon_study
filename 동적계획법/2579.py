import sys
N = int(sys.stdin.readline())
stairs = [0] * 300
answer_list = [0] * 300
for i in range(N):
    value = int(sys.stdin.readline())
    stairs[i] = value

answer_list[0] = [stairs[0], stairs[0]]
answer_list[1] = [stairs[0] + stairs[1], stairs[1]]

for i in range(2, N):
    answer_list[i] = [answer_list[i-1][1] + stairs[i], max(answer_list[i-2][0], answer_list[i-2][1]) + stairs[i]]
print(stairs)
print(answer_list)
ans = max(answer_list[N-1])

print(ans)