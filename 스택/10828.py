import sys
N = int(sys.stdin.readline())
data = []
def stack(word:str, num:int):
    if word == 'push':
        data.append(num)
    if word == 'pop':
        if len(data) > 0:
            buffer = data.pop(len(data)-1)
            print(buffer)
        elif len(data) == 0:
            print(-1)
    if word == 'size':
        print(len(data))
    if word == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    if word == 'top':
        if len(data) > 0:
            print(data[-1])
        else:
            print(-1)

for i in range(N):
    str, word, num = None, None, None
    str = sys.stdin.readline().strip()
    if str[:4] == 'push':
        word, num = str.split()
        num = int(num)

    if num == None:
        stack(str, 0)
    else:
        stack(word,num)
    