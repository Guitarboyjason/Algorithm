from collections import deque

line = input()

opener = ["[", "{", "("]
closer = ["]", "}", ")"]
while line != ".":
    stack = deque()
    balanced = True
    for i in line:
        if i in opener:
            stack.append(i)
        if i in closer:
            try:
                node = stack.pop()
                if closer.index(i) != opener.index(node):
                    print("no")
                    balanced = False
                    break

            except:
                print("no")
                balanced = False
                break
    if balanced and len(stack) > 0:
        print("no")
        balanced = False
    elif balanced:
        print("yes")
    line = input()
