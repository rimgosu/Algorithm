def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    # 만약 k가 남아있다면 뒤에서부터 제거
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)