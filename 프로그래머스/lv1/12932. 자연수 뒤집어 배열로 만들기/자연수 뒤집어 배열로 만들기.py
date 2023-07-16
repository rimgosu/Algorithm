def solution(n):
    answer = []
    n = str(n)
    n = n[::-1]
    for i in n:
        answer.append(int(i))
    return answer