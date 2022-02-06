a, b, c = map(int, input().split())
# p, q, r

def dnc(q):
    if q == 1:
        return a % c
    if q % 2 == 0:
        qq = dnc(q//2)
        return qq * qq % c
    else:
        # q % 2 == 1, 홀수인 경우
        qq = dnc(q//2)
        return qq * qq * a % c
    
print(dnc(b))