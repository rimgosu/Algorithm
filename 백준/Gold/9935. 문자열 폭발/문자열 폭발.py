a = input().rstrip()
b = input().rstrip()

stack = []

blen = len(b)

for char in a:
    stack.append(char)
    if len(stack) >= blen:
        if ''.join(stack[-blen:]) == b:
            del stack[-blen:]

if not stack:
    print('FRULA')
else:
    print(''.join(stack))
