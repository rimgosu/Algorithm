a = list(map(int, input().split()))
# print(a)
dic1 = {}
dic2 = {}
for i in range(a[0]):
    x1 = list(map(int, input().split()))
    dic1[i] = x1

for i in range(a[0]):
    x1 = list(map(int, input().split()))
    dic2[i] = x1

# print(dic1, dic2)

dic3 = {}
for i in range(len(dic1)):
    lst= []
    for j in range(len(dic1[i])):
        lst.append(dic1[i][j] + dic2[i][j]) 

    dic3[i] = lst

# print(dic3)

for i in range(len(dic3)):
    for j in range(len(dic3[i])):
        print(dic3[i][j], end=" ")
    print()