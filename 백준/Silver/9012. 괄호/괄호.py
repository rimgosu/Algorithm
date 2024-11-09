case_count = int(input())
cases = []

for _ in range(case_count):
    cases.append(input())

for case in cases:
    stack = []
    for char in case:
        if stack and stack[-1] != char:
            stack.pop()
        elif not stack and char == ')':
            stack.append(char)
            break
        else:
            stack.append(char)
    if not stack:
        print('YES')
    else:
        print('NO')