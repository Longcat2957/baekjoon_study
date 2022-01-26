import sys
N, K = map(int, sys.stdin.readline().split())
all_coin_list = []
coin_list = []
coin_num = 0
for i in range(N):
    coin_value = int(sys.stdin.readline())
    all_coin_list.append(coin_value)

# find max
for i in range(N):
    if all_coin_list[i] <= K:
        coin_list.append(all_coin_list[i])

for i in range(len(coin_list)-1, -1, -1):
    if K//coin_list[i] >= 1 and K > 0:
        coin_num += K//coin_list[i]
        K = K % coin_list[i]

print(coin_num)