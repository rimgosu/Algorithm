inp = input()
x,y = map(int, inp.split())
z = (y * 100)//x

if z == 100 or z == 99:
    print(-1)
    exit()

left = 1
right = 1000000000 ** 2

# 만약 중간점을 택했을 때 변해있다: right = mid
# 만약 중간점을 택했을 때 안변해있다: left = mid
while left <= right:
    mid = (right + left) // 2
    new_z = ((y+mid) * 100)//(x+mid)

    if new_z == z:
        left = mid +1
    else:
        right = mid -1

print(left)