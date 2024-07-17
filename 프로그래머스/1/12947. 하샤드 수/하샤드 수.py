def solution(x):
    answer = True
    x_sum = 0
    for i in str(x):
        x_sum += int(i)
        
    return True if x % x_sum == 0 else False