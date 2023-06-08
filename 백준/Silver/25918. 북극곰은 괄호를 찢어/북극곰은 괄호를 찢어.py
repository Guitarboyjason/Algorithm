N = int(input())
S = input()

max_layer = 0
stack = []
for i in S:
    if not stack or stack[-1] == i:
        stack.append(i)
    else:
        stack.pop()
    max_layer = max(max_layer, len(stack))

if stack:
    print(-1)
else:
    print(max_layer)
