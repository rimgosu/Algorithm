def solution(n):
    answer = 0
    for _n in str(n):
        answer += int(_n)
    return answer
