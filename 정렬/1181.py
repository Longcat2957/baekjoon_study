import sys
N = int(input())
message_list = []
for i in range(N):
    str = sys.stdin.readline().strip()
    length = int(len(str))
    if [length, str] not in message_list:
        message_list.append([length, str])

message_list.sort(key=lambda x : (x[0], x[1]))

for i in range(len(message_list)):
    print(message_list[i][1])
