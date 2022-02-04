import sys
input = sys.stdin.readline

string_1 = '0' + input().strip()
string_2 = '0' + input().strip()

len_string_1 = len(string_1)
len_string_2 = len(string_2)

dp = [[0 for col in range(len_string_1)]for row in range(len_string_2)]

for row in range(1, len_string_2):
    for col in range(1, len_string_1):
        if string_1[col] == string_2[row]:
            dp[row][col] = dp[row-1][col-1] + 1
        elif string_1[col] != string_2[row]:
            dp[row][col] = max(dp[row][col-1],dp[row-1][col])

print(max(dp[len_string_2 - 1]))