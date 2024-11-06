import sys
input = sys.stdin.readline
city_number, line_number, distance_info, start = map(int, input().split())
lines = {}
for i in range(line_number):
    a,b = map(int, input().split())
    if not a in lines.keys():
        lines[a] = []
    lines[a].append(b)

# bfs를 하는데,
# bfs 횟수만큼 count
queue = []
finish = {} # where: count
visited = [False] * city_number
printed = False
queue.append((start,0))
visited[start-1] = True
answer = []
while queue:
    where, count = queue.pop(0)
    if count > distance_info:
        break
    if count == distance_info:
        if finish[where] == count:
            printed = True
            answer.append(where)
    if where in lines.keys():
        for next in lines[where]:
            if not visited[next-1]:
                queue.append((next,count+1))
                visited[next-1]= True
                if not next in finish.keys():
                    finish[next] = count+1

answer.sort()
for ans in answer:
    print(ans)
if not printed:
    print(-1)