def rotate(input_list:list, k:int):
    counter = k
    o = input_list
    while counter > 0:
        a = o.pop(0)
        o.append(a)
        counter -= 1
    return o

n, k = map(int, input().split())
dataset = [x for x in range(1,n+1)]
answer = []

while True:
    dataset = rotate(dataset, k-1)
    answer.append(dataset.pop(0))
    if len(answer) == n:
        break

print('<', end ='')
for i in range(len(answer)-1):
    print(answer[i],end=', ')
print(answer[len(answer)-1], end = '')
print('>')