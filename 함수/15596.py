def solve(a: list) -> int:
    result = 0
    for c in range(len(a)):
        result += a[c]
    return result