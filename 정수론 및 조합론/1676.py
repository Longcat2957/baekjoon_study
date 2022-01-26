import math
n = int(input())
cnt_2, cnt_5 = 0, 0
for i in range(1, n+1):
    num = i
    while True:
        if num % 2 == 0:
            num = num//2
            cnt_2 += 1
        if num % 5 == 0:
            num = num//5
            cnt_5 += 1
        if num % 2 != 0 and num % 5 != 0:
            break

if cnt_2 >= cnt_5:
    cnt_2 = cnt_5
elif cnt_2 < cnt_5:
    cnt_5 = cnt_2
print(cnt_2)