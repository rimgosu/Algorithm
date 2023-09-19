a= int(input())
for _ in range(a):
    b = int(input())
    c = b//25
    d = (b%25)//10
    e = (b%25%10)//5
    f = (b%5)//1
    print(c,end=" ")
    print(d,end=" ")
    print(e,end=" ")
    print(f,end=" ")
    print()