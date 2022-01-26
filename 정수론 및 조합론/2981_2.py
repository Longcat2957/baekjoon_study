import math
n = int(input())
ans = []
int_list = []
gcd = 0
for i in range(n):
    int_list.append(int(input()))
    if i == 1:
        gcd = abs(int_list[1] - int_list[0])
    else : gcd = math.gcd(abs(int_list[i] - int_list[i-1]), gcd)
gcd_max = round(gcd**0.5)

for i in range(2, gcd_max +1):
    if gcd % i == 0:
        ans.append(i)
        ans.append(gcd//i)

ans.append(gcd)
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i, end = ' ')
    