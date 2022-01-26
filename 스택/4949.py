import sys
from string import ascii_letters

list_1 = ["()", "[]"]
list_2 = [" ", ".","\n"]

def replace(string:str):
    result = string
    for i in ascii_letters:
        result = result.replace(i,"")
    # 알파벳을 제거한다.
    for j in list_2:
        result = result.replace(j,"")
    # 공백과 마침표를 제거한다.
    while True:
        if list_1[0] in result:
            result = result.replace(list_1[0],"")
        elif list_1[1] in result:
            result = result.replace(list_1[1],"")
        else:
            break
 
    return result

string_list = []
answer_list = []
while True:
    string = sys.stdin.readline()
    if string == '.\n':
        break
    else:
        string_list.append(string)

for i in range(len(string_list)):
    a = replace(string_list[i])
    if a == '':
        answer_list.append('yes')
    else:
        answer_list.append('no')

for result in answer_list:
    print(result)