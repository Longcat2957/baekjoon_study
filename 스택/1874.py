import sys
n = int(input())
stack = []
result = []
flag = True
counter = 1
for i in range(n):
    num = int(sys.stdin.readline().strip())
    while counter <= num:
        stack.append(counter)
        result.append('+')
        counter += 1
    # 수열에 해당하는 숫자가 나올때까지 push한다.
    if stack[-1] == num:
        stack.pop(-1)
        result.append('-')
    else:
        flag = False

if flag == False:
    print('NO')
else:
    for str in result:
        print(str)