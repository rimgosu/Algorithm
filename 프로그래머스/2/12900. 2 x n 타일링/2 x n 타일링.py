"""
n=1 ans=1
n=2 ans=2
n=3 ans=3
n=4 ans=5
"""


def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n] 