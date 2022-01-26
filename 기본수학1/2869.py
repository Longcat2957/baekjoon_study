import math
a, b, v = map(int, input().split())
def function(input_a:int, input_b:int, input_v:int)-> int:
    result = (v-a)/(a-b) + 1
    return int(math.ceil(result))
print(function(a,b,v))