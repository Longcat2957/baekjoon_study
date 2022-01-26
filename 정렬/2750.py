import sys
n = sys.stdin.readline().strip()
n = int(n)
empty_list = []
for i in range(n):
    buffer = sys.stdin.readline().strip()
    buffer = int(buffer)
    empty_list.append(buffer)

empty_list = sorted(empty_list)

for i in range(len(empty_list)):
    print(empty_list[i])