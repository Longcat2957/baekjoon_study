n = int(input())
list = list(map(float, input().split()))
max = max(list)
ave = 0
result = []
for num in list:
    result.append((num/max)*100)
for num in result:
    ave += num
print((ave/n))