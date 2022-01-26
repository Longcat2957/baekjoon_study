n, x = map(int, input().split())
input_list = list(map(int, input().split()))
result_list = []
for c in range(len(input_list)):
    if input_list[c] < x:
        result_list.append(input_list[c])
    else:
        continue
for i in range (len(result_list)):
    print(result_list[i], end = ' ')