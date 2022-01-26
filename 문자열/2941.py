def check_croatia(input:list)-> bool:
    if input in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
        return True
    else:
        return False
def count_croatia(input:list)-> int:
    counter = 0
    for i in range(len(input)-1):
        if check_croatia(input[i]+input[i+1]) == True:
            counter += 1
    for i in range(len(input)-2):
        if check_croatia(input[i]+input[i+1]+input[i+2]) == True:
            counter += 1
    return counter

def return_croatia(input:list)-> int:
    return len(input) - count_croatia(input)

input_string = input()
print(return_croatia(input_string))