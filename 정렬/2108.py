import sys
import statistics
N = int(sys.stdin.readline())
data_list = []
for i in range(N):
    num = int(sys.stdin.readline())
    data_list.append(num)

# 산술평균, 중앙값, 최빈값, 범위를 출력
print(round(statistics.mean(data_list)))
print(statistics.median(data_list))
if len(statistics.multimode(data_list)) >= 2:
    buffer_list = statistics.multimode(data_list)
    buffer_list.remove(min(buffer_list))
    print(min(buffer_list))
else:
    print(statistics.mode(data_list))
print(max(data_list) - min(data_list))