def solution(land):
    n = len(land)  # 행의 개수
    dp = [[0] * 4 for _ in range(n)]  # dp[i][j]: i번째 행의 j열을 선택했을 때의 최대 점수

    # 첫 번째 행의 초기값 설정
    dp[0] = land[0]

    # 두 번째 행부터 마지막 행까지 반복
    for i in range(1, n):
        for j in range(4):
            # 이전 행에서 현재 열과 겹치지 않는 열의 최대 점수를 선택하여 현재 행의 최대 점수에 더함
            dp[i][j] = max(dp[i - 1][:j] + dp[i - 1][j + 1:]) + land[i][j]

    # 마지막 행의 최대 점수 중 가장 큰 값을 반환
    return max(dp[n - 1])