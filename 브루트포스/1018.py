n, m = map(int, input().split())
input_string = []
for i in range(n):
    input_string.append(input().strip())

def check_64(striped_list:list) -> int:
    buffer_list = striped_list
    counter1, counter2 = 0, 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if buffer_list[i][j] == 'W':
                    counter1 += 1
                if buffer_list[i][j] == 'B':
                    counter2 += 1
            elif (i+j) % 2 == 1:
                if buffer_list[i][j] == 'B':
                    counter1 += 1
                if buffer_list[i][j] == 'W':
                    counter2 +=1
    return min([counter1, counter2])

def strip_64(original_list:list, x:int, y:int) -> list:
    buffer_list = original_list[y:y+8]
    for i in range(8):
        buffer_list[i] = buffer_list[i][x:x+8]
    return buffer_list

def find_min_value(original_list:list) -> int:
    empty_list = []
    n = len(original_list) - 8 + 1
    m = len(original_list[0]) - 8 + 1
    for i in range(m):
        for j in range(n):
            striped_list = strip_64(original_list, i, j)
            empty_list.append(check_64(striped_list))
    print(min(empty_list))
            
find_min_value(input_string)