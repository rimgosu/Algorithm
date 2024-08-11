def solution(absolutes, signs):
    answer = 0
    for index, absolute in enumerate(absolutes):
        if signs[index]:
            answer += absolute
        else:
            answer -= absolute
    return answer