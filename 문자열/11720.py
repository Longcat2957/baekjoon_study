n = int(input())
int_list = list(map(int, str(input())))
sum = 0
for num in range(len(int_list)):
    sum += int_list[num]
print(sum)