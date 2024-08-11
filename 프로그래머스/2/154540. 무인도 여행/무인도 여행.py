from collections import deque

def solution(maps):
    answer = []
    n,m = len(maps[0]), len(maps)
    island_solved = [[-1 for i in range(n)] for i in range(m)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    solved_set = set()
    
    for i in range(n):
        for j in range(m):
            if maps[j][i] == 'X':
                continue
            if (i,j) in solved_set:
                continue
            visited = [[False for k in range(n)] for l in range(m)]
            island_area = 0
            queue = deque()
            queue.append((i,j))
            visited[j][i] = True
            solved_set.add((i,j))
            duplication = False
            
            while queue:
                x, y = queue.pop()
                island_area += int(maps[y][x])
                
                for dx, dy in directions:
                    if 0 <= x+dx < n and 0<= y+dy < m and \
                    not visited[y+dy][x+dx] and maps[y+dy][x+dx] != 'X':
                        queue.append((x+dx, y+dy))
                        visited[y+dy][x+dx] = True
                        solved_set.add((x+dx,y+dy))
                        
            island_solved[j][i] = island_area
            answer.append(island_area)
                
    answer.sort()
                        
    return answer if answer else [-1]