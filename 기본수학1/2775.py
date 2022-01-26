# 2775
def return_number(a:int, b:int)->int:
    result_list = []
    buffer_list = []
    counter = a
    for c in range(1, 15):
        result_list.append(int(c))
        # result_list = [1, 2, 3, 4 ... 14]
    while True:
        if counter == 0:
            return result_list[b-1]
        else:
            for c in range(b):
                buffer_list.append(sum(result_list[0:c+1]))
            result_list = buffer_list
            buffer_list = []
            counter -= 1

t = int(input())
empty_list = []
for i in range(t):
    a = int(input())
    b = int(input())
    empty_list.append([a,b])

for i in range(t):
    print(return_number(empty_list[i][0], empty_list[i][1]))