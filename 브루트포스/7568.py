n = int(input())
list = []
result_list = []
for i in range(n):
    w, h = map(int, input().split())
    list.append([w, h])

for i in range(n):
    counter = 1
    buffer = list[i]
    for data in list:
        if buffer[0] < data[0] and buffer[1] < data[1]:
            counter +=1
    result_list.append(counter)

for i in range(len(result_list)):
    print(result_list[i], end=' ')