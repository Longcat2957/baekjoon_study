import sys
N = sys.stdin.readline()
list_1 = set(sys.stdin.readline().split())
M = sys.stdin.readline()
list_2 = sys.stdin.readline().split()

for i in list_2:
    if i in list_1:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')