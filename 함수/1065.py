def han(input:int)->bool:
    buffer = []
    buffer = list(map(int, str(input)))
    if len(buffer) > 3:
        for c in range(1, len(buffer)-2):
            try:
                if buffer[0]-buffer[1] != buffer[c] - buffer[c+1]:
                    return False
                return True
            except:
                 return False
    elif len(buffer) == 3:
        if buffer[0] - buffer[1] == buffer[1] - buffer[2]:
            return True
        else:
            return False
    elif len(buffer) <= 2:
        return True
def count_han(input:int)->int:
    counter = 0
    for num in range(1, input+1):
        if han(num) == True:
            counter += 1
    print(counter)
    return counter
n = int(input())
count_han(n)