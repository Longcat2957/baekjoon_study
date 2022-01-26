def sum_ten_one(input_int):
    return input_int // 10 + input_int % 10
def convert(input_int):
    if sum_ten_one(input_int) < 10:
        return 10*(input_int%10) + sum_ten_one(input_int)
    else:
        return 10*(input_int%10) + sum_ten_one(input_int)%10

n = int(input())
buffer = 0
c = 0
while True:
    if c == 0:
        buffer = convert(n)
    else:
        buffer = convert(buffer)
    c += 1
    if n == buffer:
        break
print(c)