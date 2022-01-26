import sys

N = int(sys.stdin.readline())
house_list = []
for _ in range(N):
    R, G, B = map(int, sys.stdin.readline().split())
    house_list.append([R, G, B])

for i in range(1, N):
    house_list[i][0] = house_list[i][0] + min(house_list[i-1][1], house_list[i-1][2])
    house_list[i][1] = house_list[i][1] + min(house_list[i-1][0], house_list[i-1][2])
    house_list[i][2] = house_list[i][2] + min(house_list[i-1][0], house_list[i-1][1])

print(min(house_list[N-1]))