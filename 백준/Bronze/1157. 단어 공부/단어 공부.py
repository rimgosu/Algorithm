a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic = {}
for i in a:
    dic[i] = 0

inp = input()

for i in inp:
    dic[i.upper()] += 1

ma = 0
for i in a:
    if dic[i] > ma : 
        ma= dic[i] 

lst = []   
for i in a:
    if dic[i] == ma:
        lst.append(i)


if len(lst) == 1 :
    print(lst[0])
else :
    print("?")