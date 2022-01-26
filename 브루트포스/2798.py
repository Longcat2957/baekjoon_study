n, m = map(int, input().split())
card_list = list(map(int, input().split()))
card_list.sort()
result_list = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = card_list[i] + card_list[j] + card_list[k]
            if sum <= m:
                result_list.append(int(sum))
print(max(result_list))