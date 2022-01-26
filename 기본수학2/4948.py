import math
input_list = []
while True:
    input_value = int(input())
    if input_value == 0:
       break
    else:
        input_list.append(input_value)
min_value, max_value = min(input_list), max(input_list)
prime_list = []
for i in range(min_value, 2*max_value+1):
    max_value = round(math.sqrt(i))
    flag = True
    for c in range(2, max_value+1):
        if i % c == 0:
            flag = False
            break
    if flag == True:
        prime_list.append(i)
if 1 in prime_list:
    prime_list.remove(1)

for c in range(len(input_list)):
    value = input_list[c]
    counter = 0
    for prime in prime_list:
        if value < prime <= 2* value:
            counter +=1
    print(counter)
