inp = int(input())
level_score = []
for _ in range(inp):
    level_score.append(int(input()))

last_num = level_score.pop() # 5
answer = 0
while level_score:
    now_num = level_score.pop() # 6
    while now_num >= last_num:
        now_num -= 1
        answer +=1
    last_num = now_num

print(answer)
        