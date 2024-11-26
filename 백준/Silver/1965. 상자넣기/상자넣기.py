num = int(input())
dp = [1] * num

lst = list(map(int, input().split()))

for i in range(num):
    _max = 0
    for j in range(i):
        if dp[j] > _max and lst[i] > lst[j]:
            _max = dp[j]
            dp[i] = dp[j] + 1

print(max(dp))