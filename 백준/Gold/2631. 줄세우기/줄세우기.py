num = int(input())
lst = []
dp = [1]*num
for i in range(num):
    lst.append(int(input()))

for i in range(num):
    _max = 0
    for j in range(i):
        if dp[j] > _max and lst[j] < lst[i]:
            _max = dp[j]
            dp[i] = dp[j] + 1

print(num - max(dp))