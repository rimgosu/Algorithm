# 생성, 복제
target_number = int(input())

try_count, cats = 0, 0
while cats < target_number:
    if cats == 0:
        cats +=1
        try_count +=1
    else:
        cats *=2
        try_count +=1

print(try_count)