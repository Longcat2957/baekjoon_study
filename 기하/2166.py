n = int(input())
x_list, y_list = [], []
s_sum = 0

for i in range(n):
    a, b = map(int, input().split())
    x_list.append(a)
    y_list.append(b)

x_list.append(x_list[0])
y_list.append(y_list[0])

for i in range(n):
    s_sum += (x_list[i] * y_list[i+1]) - (y_list[i] * x_list[i+1])

s_sum = round(abs(s_sum)/2, 1)
print(s_sum)