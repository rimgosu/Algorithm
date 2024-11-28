num = int(input())
lst = list(map(int, input().split()))
dp = [1] * num

for i in range(num):
    _max = 0
    for j in range(i):
        if _max < dp[j] and lst[i] > lst[j]:
            _max = dp[j]
            dp[i] = dp[j]+1

lst = lst[::-1]
dp2 = [1] * num

for i in range(num):
    _max = 0
    for j in range(i):
        if _max < dp2[j] and lst[i] > lst[j]:
            _max = dp2[j]
            dp2[i] = dp2[j]+1

print(max([a+b-1 for a,b in zip(dp,dp2[::-1])]))
