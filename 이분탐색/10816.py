n = int(input())
int_list = list(map(int, input().split()))

dict = dict()
for num in int_list:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

m = int(input())
int_list_2 = list(map(int, input().split()))

for num in int_list_2:
    if num in dict:
        print(dict[num], end=' ')
    else:
        print(0, end=' ')