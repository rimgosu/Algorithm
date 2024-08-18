
def solution(triangle):
    dp = [[] for i in range(len(triangle))]
    
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            left_num, right_num, next_num = 0,0,0
            try:
                left_num = dp[i-1][j]
            except:
                pass
            try:
                right_num = dp[i-1][j-1]
            except:
                pass
            
            # 왼쪽
            if j == 0 :
                next_num = left_num + triangle[i][j]
            # 오른쪽
            elif j == len(triangle[i]) -1:
                next_num = right_num + triangle[i][j]
            # 중간
            else:
                next_num = max(left_num, right_num) + triangle[i][j]
            dp[i].append(next_num)
    
    return max(dp[-1])