import sys

input = sys.stdin.readline

T = int(input())
# T 는 테스트 케이스의 수 이다.
answers = []
for _ in range(T):
    n = int(input())
    class_dict = dict()
    # n은 해빈이가 가진 의상의 수 이다.
    for wears in range(n):
        w, c = input().split()
        if c not in class_dict:
            class_dict[c] = 1
        elif c in class_dict:
            class_dict[c] += 1
    sum = 1
    for classes in class_dict:
        sum *= (class_dict[classes] + 1)
    
    answers.append(sum - 1)
    
print(*answers,sep='\n')
    
        
        
    
    
    
    
    