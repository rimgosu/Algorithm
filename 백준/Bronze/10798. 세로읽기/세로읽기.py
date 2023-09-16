dic = {}
for i in range(5):
    dic[i] = input()

maxlen = 0
for i in range(len(dic)):
    if len(dic[i]) > maxlen:
        maxlen = len(dic[i])


for i in range(5):
    while len(dic[i])< maxlen:
        dic[i] += "?"



for i in range(maxlen):
    for j in range(5):
        if dic[j][i] != '?':
            print(dic[j][i], end="")