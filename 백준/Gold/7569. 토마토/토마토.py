import sys
from collections import deque
input = sys.stdin.readline

x,y,z = map(int,input().split())

tomato_box = []
for i in range(z):
    xy_line = []
    for j in range(y):
        x_line = list(map(int, input().split()))
        xy_line.append(x_line)
    tomato_box.append(xy_line)

# 만약 '0'이 없으면 0 출력하고 종료
zero_contained = False 
queue = deque()
for dz in range(z):
    for dy in range(y):
        for dx in range(x):
            if tomato_box[dz][dy][dx] == 1:
                queue.append(((dx,dy,dz), 0))
            else:
                zero_contained = True

if not zero_contained:
    print(0)
    exit()

directions = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]
ans = 0
while queue:
    coordinate, count = queue.popleft()
    nx,ny,nz = coordinate
    ans = count 
    
    for dx,dy,dz in directions:
        mx,my,mz = nx+dx, ny+dy, nz+dz
        if 0 <= mx < x and 0 <= my < y and 0 <= mz < z and tomato_box[mz][my][mx] == 0:
            queue.append(((mx,my,mz), count+1))
            tomato_box[mz][my][mx] = 1

zero_contained = False 
queue = []
for dz in range(z):
    for dy in range(y):
        for dx in range(x):
            if tomato_box[dz][dy][dx] == 0:
                zero_contained = True

if zero_contained:
    print(-1)
else:
    print(ans)