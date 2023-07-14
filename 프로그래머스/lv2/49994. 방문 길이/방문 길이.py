def solution(dirs):
    answer = 0
    dic = {}
    cur = [0,0]
    # print(dic)
    for d in dirs:
        if d == 'U' and cur[1] != 5:
            # print("up")
            if tuple(cur) in dic:
                if 'U' in dic[tuple(cur)]:
                    pass
                else:
                    dic[tuple(cur)] += 'U'
            else:
                dic[tuple(cur)] = 'U'
            cur[1] +=1
            if tuple(cur) in dic:
                if 'D' in dic[tuple(cur)]:
                    pass
                else:
                    dic[tuple(cur)] += 'D'
            else:
                dic[tuple(cur)] = 'D'
        elif d == 'D' and cur[1] != -5:
            # print("down")
            if tuple(cur) in dic:
                if 'D' in dic[tuple(cur)]:
                    pass
                else:
                    dic[tuple(cur)] += 'D'
            else:
                dic[tuple(cur)] = 'D'
            cur[1] -=1
            if tuple(cur) in dic:
                if 'U' in dic[tuple(cur)]:
                    pass
                else:
                    dic[tuple(cur)] += 'U'
            else:
                dic[tuple(cur)] = 'U'
        elif d == 'R' and cur[0] != 5:
            # print("right")
            if tuple(cur) in dic:
                if 'R' in dic[tuple(cur)]:
                    pass
                else:
                    dic[tuple(cur)] += 'R'
            else:
                dic[tuple(cur)] = 'R'
            cur[0] +=1
            if tuple(cur) in dic:
                if 'L' in dic[tuple(cur)]:
                    pass
                else:
                    dic[tuple(cur)] += 'L'
            else:
                dic[tuple(cur)] = 'L'
        elif d == 'L' and cur[0] != -5:
            # print("left")
            if tuple(cur) in dic:
                if 'L' in dic[tuple(cur)]:
                    pass
                else:
                    dic[tuple(cur)] += 'L'
            else:
                dic[tuple(cur)] = 'L'
            cur[0] -=1
            if tuple(cur) in dic:
                if 'R' in dic[tuple(cur)]:
                    pass
                else:
                    dic[tuple(cur)] += 'R'
            else:
                dic[tuple(cur)] = 'R'
        # print("cur", cur)
    print("dic", dic)
    for index, value in dic.items():
        answer += len(value)
    return answer//2


# print(solution("RRRRRLLLLL"))