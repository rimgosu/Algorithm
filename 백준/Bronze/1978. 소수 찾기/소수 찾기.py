a = int(input())
b = list(map(int, input().split()))

# print(a, b)

def sosu(num):
    if num == 1:
        return 0
    for i in range(2,num):
        c = 0
        if num % i == 0 :
            return 0
    return 1

d = 0
for i in b:
    d += sosu(i)

print(d)
