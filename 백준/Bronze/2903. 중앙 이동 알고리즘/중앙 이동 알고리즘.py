import sys


a = int(input())
b = 0


dic = {1:3}

for i in range(2,16):
    dic[i] = dic[i-1] + (dic[i-1]-1)

print(
    dic[a]*dic[a]
)
