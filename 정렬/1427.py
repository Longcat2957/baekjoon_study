import sys
N = list(sys.stdin.readline().strip())
ans = sorted(N)
string = ''
for char in ans[::-1]:
    string += char

print(string)