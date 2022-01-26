x, y, w, h = map(int, input().split())
def find_min_path(x:int, y:int, width:int, height:int):
    path_list = []
    path_list.append(x)
    path_list.append(y)
    path_list.append(width-x)
    path_list.append(height-y)
    min_path = min(path_list)
    print(min_path)

find_min_path(x, y, w, h)