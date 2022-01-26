N = int(input())

def prime_factorization(input:int) -> str:
    if input == 1:
        return
    buffer = input
    for d in range(2, input+1):
        while True:
            if buffer % d == 0:
                print(d)
                buffer = buffer // d
            elif buffer % d != 0:
                break
prime_factorization(N)