num = int(input())
dp = [0] * num
lst = list(map(int,input().split()))

# 10 30 10 20 20 10
# 1  1  2  2  2  3
# 1. 자기 이전 자기보다 큰 값
# 2. 자기보다 큰 값중 dp가 최대인것

for i in range(num):
    # print(i)
    if i == 0:
        dp[i] = 1
        continue
    # 자기보다 작은 값
    left_idx = i - 1
    now_num = lst[i]
    max_dp = 0
    for j in range(left_idx+1):
        prev_num = lst[j]
        # print(prev_num)
        if prev_num > now_num and max_dp < dp[j]:
            # print('prev_num:', prev_num, 'now_num:', now_num)
            max_dp = dp[j]
            dp[i] = dp[j] + 1
    if dp[i] == 0:
        dp[i] = 1

print(max(dp))
# 12
# 10 30 10 20 20 10 0 30 10 20 20 10

