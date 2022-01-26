import sys

def find_max(n, array:list):
    stack = []
    answer = 0
    for height in array:
        tmp = 0
        while len(stack) != 0 and stack[-1][0] > height:
            tmp += stack[-1][1]
            answer = max(answer, tmp * stack[-1][0])
            stack.pop()
        tmp += 1
        stack.append([height, tmp])
    tmp = 0
    while len(stack) != 0:
        tmp += stack[-1][1]
        answer = max(answer, tmp * stack[-1][0])
        stack.pop()
    return answer

answer_list = []

while True:
    string = sys.stdin.readline().strip()
    if string == '0':
        break
    else:
        data = list(map(int, string.split()))
        n = data.pop(0)
        answer_list.append(find_max(n, data))
        # n과 정수 리스트로 입력받은 스트링을 분리하여 각 변수에 저장한다.

for ans in answer_list:
    print(ans)