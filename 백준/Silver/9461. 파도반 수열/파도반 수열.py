dp = [0] * 100
for number in range(1,101):
    if number == 1: dp[0] = 1
    elif number == 2: dp[1] = 1
    elif number == 3: dp[2] = 1
    else: dp[number-1] = dp[number-3] + dp[number-4]

case_num = int(input())
for _ in range(case_num):
    print(dp[int(input())-1])