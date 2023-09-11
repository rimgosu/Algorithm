a = input().split()
b = input()
a_min = int(a[0]) * 60 + int(a[1])
sum_min = (a_min + int(b)) % (60 * 24)
sum_hour = sum_min//60
sum_min = sum_min%60
print(sum_hour,sum_min)