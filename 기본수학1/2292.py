import math
# 2292번
n = int(input())
def find_layer(input: int) -> int:
    result = ((-3)+math.sqrt(12*input-3))/(6)
    if result == 0:
        return 0
    else:
        return int(math.ceil(result))
print(find_layer(n)+1)