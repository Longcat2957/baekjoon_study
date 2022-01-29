import sys
from string import ascii_letters
from collections import defaultdict
N, M = map(int, sys.stdin.readline().split())

poke_dict = defaultdict()
poke_dict_r = defaultdict(str)
for i in range(N):
    name = sys.stdin.readline().strip()
    poke_dict[i+1] = name
    poke_dict_r[name] = i+1

problem_list = []
for _ in range(M):
    name = sys.stdin.readline().strip()
    problem_list.append(name)

answer_list = []
for pb in problem_list:
    if str(pb)[0] in ascii_letters:
        answer_list.append(poke_dict_r[pb])
    else:
        answer_list.append(poke_dict[int(pb)])
        
print(*answer_list,sep='\n')