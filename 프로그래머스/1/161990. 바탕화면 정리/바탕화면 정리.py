def solution(wallpaper):
    answer = [] # [y좌표 min, x좌표 min,  y좌표 max, x좌표 max]
    
    width, height = len(wallpaper[0]), len(wallpaper)
    
    ymin, xmin, ymax, xmax = 100,100,0,0
    
    for y in range(height):
        for x in range(width):
            if wallpaper[y][x] == '#':
                if y < ymin:
                    ymin = y
                if x < xmin:
                    xmin = x
                if y+1 > ymax:
                    ymax = y+1
                if x+1 > xmax:
                    xmax = x+1
    return [ymin,xmin,ymax,xmax]