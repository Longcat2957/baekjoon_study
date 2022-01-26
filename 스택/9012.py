import sys

def check_VPS(str):
    copy = str
    while True:
        if '()' in copy:
            copy = copy.replace('()',"")
        elif '()' not in copy:
            break

    if copy == "":
        ans = True
    else:
        ans = False

    if ans == True:
        return 'YES'
    else:
        return 'NO'
        


T = int(sys.stdin.readline())
answer_list = []
for i in range(T):
    str = sys.stdin.readline().strip()
    answer_list.append(check_VPS(str))
    
for i in range(len(answer_list)):
    print(answer_list[i])