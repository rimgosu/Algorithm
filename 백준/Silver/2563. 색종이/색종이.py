a = [[0 for _ in range(100)] for _ in range(100)]
b = int(input())
for i in range(b):
    x,y = map(int, input().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            a[j][k] = 1

_sum = 0
for i in range(len(a)):
    _sum += sum(a[i])
print(_sum)