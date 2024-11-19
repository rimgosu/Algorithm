def solution(numbers):
    def is_sosu(number):
        if number <2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    answers = set()
    def dfs(now, remain):
        if now and is_sosu(int(now)):
            answers.add(int(now))
        if not remain:
            return
        
        for idx, r in enumerate(remain):
            next_remain = remain[:idx] + remain[idx+1:] 
            dfs(now+r,next_remain)
    
    dfs('', numbers)
    return len(answers)        
