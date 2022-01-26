N, K = map(int, input().split())
num1, num2, num3 = N, K, N - K

def count_num(n,k):
    count = 0
    while n:
        n //= k
        count += n
    return count

cnt_5 = count_num(num1, 5) - count_num(num2, 5) - count_num(num3, 5)
cnt_2 = count_num(num1, 2) - count_num(num2, 2) - count_num(num3, 2)
result = min(cnt_2, cnt_5)

print(result)