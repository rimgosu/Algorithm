a,b = input().split()
a = a.upper()
b = int(b) 
# print(a)

A = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dic = {}
for i, value in enumerate(A):
    dic[value] = i
# print(dic)

arev = a[::-1]
asum = 0
for i, value in enumerate(arev):
    # print(i, value, b**i )
    asum += dic[value] * (b ** i)

print(asum)