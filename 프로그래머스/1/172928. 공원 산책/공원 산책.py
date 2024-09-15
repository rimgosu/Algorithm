def solution(park, routes):
    width, height = len(park[0]), len(park) 
    
    location_now = (0,0)
    for y in range(height):
        for x in range(width):
            if park[y][x] == 'S':
                location_now = (y,x)
                break
    
    for route in routes:
        dx, dy = 0, 0
        direction, num = route.split()
        num = int(num)
        now_y, now_x = location_now
        can_move = True
        if direction == 'E':
            dx = num
            for x in range(1,dx+1):
                if now_x + x >= width or park[now_y][now_x+x] == 'X':
                    can_move = False
                    break
        elif direction == 'W':
            dx = -num
            for x in range(1,abs(dx)+1):
                if 0 > now_x - x or park[now_y][now_x- x] == 'X':
                    can_move = False
                    break
        elif direction == 'S':
            dy = num
            for y in range(1,dy+1):
                if now_y + y >= height or park[now_y+y][now_x] == 'X':
                    can_move = False
                    break
        else:
            dy = -num
            for y in range(1,abs(dy)+1):
                if 0 > now_y - y or park[now_y-y][now_x] == 'X':
                    can_move = False
                    break


        
        if can_move:
            location_now = (now_y+dy,now_x+dx)
    return [location_now[0], location_now[1]]