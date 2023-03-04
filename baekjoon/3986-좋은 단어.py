N = int(input())
words = [list(input())for _ in range(N)]
cnt = 0
for word in words:
    stack = list()
    for char in word:
        if not stack:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
    if len(stack) == 0:
        cnt += 1
print(cnt)