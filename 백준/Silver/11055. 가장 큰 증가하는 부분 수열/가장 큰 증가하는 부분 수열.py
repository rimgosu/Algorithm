num = int(input())
lst = list(map(int,input().split()))
dp = [i for i in lst]
for i in range(num):
    _max = 0
    for j in range(i):
        if lst[j] < lst[i] and _max < dp[j]:
            dp[i] = dp[j] + lst[i]
            _max = dp[j]
    
print(max(dp))
