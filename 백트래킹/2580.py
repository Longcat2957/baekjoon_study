import sys

def horizontal(y, number:int):
    if number in matrix[y]:
        return False
    return True

def vertical(x, number:int):
    for i in range(9):
        if number == matrix[i][x]:
            return False
    return True

def square(y, x, number:int):
    ny = 3 * (y//3)
    nx = 3 * (x//3)
    for i in range(3):
        for j in range(3):
            if matrix[ny+i][nx+j] == number:
                return False
    return True

def DFS(index):
    if index == len(zero):
        for i in range(9):
            print(*matrix[i], sep = ' ')
        exit()
    else:
        yy, xx = zero[index]
        for i in range(1, 10):
            if horizontal(yy, i) and vertical(xx, i) and square(yy, xx, i):
                matrix[yy][xx] = i
                DFS(index + 1)
                matrix[yy][xx] = 0
                # if failed
                


matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero = [(y, x) for y in range(9) for x in range(9) if matrix[y][x] == 0]
DFS(0)