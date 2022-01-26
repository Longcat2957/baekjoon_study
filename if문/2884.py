num1, num2 = map(int, input().split())
result = 60 * num1 + num2 - 45
hour = result // 60
if hour < 0:
    hour += 24
minute = result % 60
print(hour, minute)