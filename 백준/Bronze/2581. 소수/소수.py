sos = []


def sosu(num):
    if num == 1:
        return 0
    for i in range(2,num):
        c = 0
        if num % i == 0 :
            return 0
    return 1



for i in range(1,10001):
    if sosu(i) == 1:
        sos.append(i)

# print(sos)

a = int(input())
b = int(input())

answer = []
for i in range(a,b+1):
    if i in sos:
        answer.append(i)

if answer == []:
    print('-1')
else:
    print(sum(answer))
    print(min(answer))

