l = input().split()
total_min = int(l[0]) * 60 + int(l[1]) - 45
if total_min >= 0 :
    hour = total_min//60
    min_ = total_min%60
    print(hour,min_)
else : 
    hour = total_min//60 + 24
    min_ = total_min%60
    print(hour,min_)