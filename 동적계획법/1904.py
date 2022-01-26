import sys
N = int(sys.stdin.readline())
tile_list = [0] * 1000001
tile_list[1] = 1
tile_list[2] = 2

for i in range(3, N+1):
    tile_list[i] = (tile_list[i-1] + tile_list[i-2])%15746

ans = tile_list[N]
print("{}".format(ans))