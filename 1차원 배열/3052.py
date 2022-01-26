raw_list = []
while True:
    try:
        raw_list.append(int(input()))
    except:
        break
result_list = []
for num in raw_list:
    if num%42 not in result_list:
        result_list.append(num%42)
print(len(result_list))