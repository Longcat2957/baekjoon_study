import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    data.append([x, y])

data.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(data[i][0], data[i][1])