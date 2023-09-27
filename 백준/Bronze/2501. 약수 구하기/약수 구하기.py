a,b = map(int, input().split())
b-=1
# print(a,b)

lst = []
for i in range(1,a+1):
    if a % i == 0 :
        lst.append(i)

try: 
    print(lst[b]) 
except:
    print(0)