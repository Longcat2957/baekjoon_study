import sys
number_of_city = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
oil_price = list(map(int, sys.stdin.readline().split()))
cost = oil_price[0]
total_price = 0

for i in range(number_of_city - 1):
    if cost > oil_price[i]:
        cost = oil_price[i]
    total_price += cost * distance[i]
    
print(total_price)