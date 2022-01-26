import sys

N = int(sys.stdin.readline())
data = []
for i in range(N):
    num, name = sys.stdin.readline().strip().split()
    num = int(num)
    data.append([num, name])

data.sort(key=lambda x : x[0])

for i in range(len(data)):
    print(data[i][0], data[i][1])