inp = int(input())

str_order = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dic = {}
for i in range(len(str_order)):
    dic[str_order[i]] = i

for _ in range(inp):
    _ = int(input())
    str_lst = input().split()
    str_lst = str_lst[::-1]
    answer = str_lst.pop()
    while str_lst:
        now = str_lst.pop()
        if dic[answer[0]] >= dic[now]:
            now += answer
            answer = now
        else:
            answer += now
    print(answer)