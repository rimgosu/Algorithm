def solution(arr, divisor):
    answer = []
    for a in arr:
        if a%divisor == 0:
            answer.append(a)
    answer.sort()
    return answer if not answer ==[] else [-1]