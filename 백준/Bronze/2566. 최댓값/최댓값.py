dic = {}
for i in range(9):
    dic[i]= list(map(int, input().split()))
_max, x, y = 0, 1, 1
for i in range(len(dic)):
    for j in range(len(dic[i])):
        if dic[i][j] > _max:
            _max = dic[i][j]
            x = i+1
            y = j+1
print(_max)
print(x,y)