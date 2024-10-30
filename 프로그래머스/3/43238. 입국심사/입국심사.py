def solution(n, times):
    answer = 0
    
    # 특정 시간이 주어졌을 때 몇개 처리 가능?
    # 28
    # 28 // 7, 28 // 10
    
    left, right = 1, 1000000000 * n
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid가 n보다 크면? mid를 줄여야함 - right = mid-1
        # 그렇지 않으면?
        
        ans = 0
        for time in times:
            ans += mid // time
        
        if ans >= n:
            right = mid -1
        else:
            left = mid +1
        
    
    return left