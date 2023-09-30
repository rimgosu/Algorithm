x,y,w,h = map(int, input().split())
lst =[]
lst.append(x)
lst.append(y)
lst.append(abs(w-x))
lst.append(abs(y-h))

print(min(lst))