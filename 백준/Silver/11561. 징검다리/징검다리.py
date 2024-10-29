# 4
# 1
# 2
# 100
# 1000000

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6 ...
# print(13*14/2) # 100 이전
# print(1413*1414/2) # 1000000 이전
# print(1*2/2) # 

# 9일 때
# 1 3 6 10

# ans(ans+1)/2 <= n, break, print(ans-1)

# inp = input().strip().split('\n')
# inp = inp[1:]
# inp = list(map(int, inp))
# print(inp)

N = int(input())
inputs = []
for i in range(N):
    inputs.append(int(input()))

# print(inputs)

for i in inputs:
    # while ans*(ans+1)/2 <= i:
    left, right = 1, 10 ** 16
    while left <= right:
        mid = (left + right) //2
        # i가 만약 mid * (mid +1) /2 보다 작으면 left = mid + 1
        if mid * (mid + 1) / 2 <= i:
            left = mid +1
        else:
            right = mid -1

    print(left-1)