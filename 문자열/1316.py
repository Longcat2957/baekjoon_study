N = int(input())
empty_list = []
for i in range(N):
    empty_list.append(input())
for i in range(N):
    word = empty_list[i]
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            N -= 1
            break
print(N)