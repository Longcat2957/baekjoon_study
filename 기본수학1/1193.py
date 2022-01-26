# 1193
import math
n = int(input())
def find_sum(input:int)->int:
    result = math.ceil(((-1)+math.sqrt(1+8*input))/(2))
    return result

def find_answer(input:int)->list:
    sum = find_sum(input)
    num = input - ((sum-1)*(sum))/(2)
    num = int(num)
    if sum % 2 == 0:
        return str(num)+'/'+str(sum+1-num)
    else:
        return str(sum+1-num)+'/'+str(num)
print(find_answer(n))