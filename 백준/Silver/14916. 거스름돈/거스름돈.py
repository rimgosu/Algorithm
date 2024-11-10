inp= int(input())
num=0
if inp == 3 or inp == 1:
    print(-1)
    exit()
    
while inp >= 5:
    num = inp // 5
    inp = inp % 5
if inp % 2 == 1:
    num -= 1
    inp += 5
num += inp // 2
print(num)