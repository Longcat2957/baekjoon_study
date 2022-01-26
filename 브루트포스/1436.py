n = int(input())

def jongmal(input:int) -> bool:
    buffer = str(input)
    if buffer.count('666') >= 1:
        return True
    else:
        return False

def make_jongmal() -> list:
    empty_list = []
    for i in range(2800000):
        if jongmal(i) == True:
            empty_list.append(i)
        else:
            continue
    return empty_list

result_list = make_jongmal()
print(result_list[n-1])