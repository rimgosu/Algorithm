
n,m = map(int, input().split())

trees=list(map(int, input().split()))
# print(trees)

left, right = 1, max(trees) * 10
answer = 0

while left <= right:
    mid = (left + right) // 2

    sums = 0
    for tree in trees:
        remain = tree - mid
        if remain > 0:
            sums += remain    
    # 만약 m보다 크면 mid 높인다
    # 만약 m보다 작으면 mid 낮추고

    if sums >= m:
        answer = mid
        left = mid +1
    else:
        right = mid -1

print(answer)
        