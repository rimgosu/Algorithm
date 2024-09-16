def solution(mats, park):
    answer = -1
    width, height = len(park[0]), len(park)
    for x in range(width):
        for y in range(height):
            if park[y][x] == '-1':
                for a in mats:
                    can_install = True
                    try:
                        for dx in range(a):
                            for dy in range(a):
                                if park[y+dy][x+dx] != '-1':
                                    can_install = False
                                    break
                    except:
                        can_install = False
                    if can_install:
                        if a > answer:
                            answer = a
    return answer