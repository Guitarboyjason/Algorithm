
stack = []
pair = dict()
pair['('] = ')'
pair['['] = ']'
pair[')'] = '('
pair[']'] = '['
line = input()
summary = 0
tmp = 1
flag = False
for i in line:
    if i == '(' or i == '[':
        stack.append(i)
        flag = True
        if i == "(":
            tmp *= 2
        else:
            tmp *= 3
    if i == ')' or i == ']':
        if len(stack) == 0 or pair[i] != stack.pop():
            summary = 0
            break
        else:
            if flag:
                summary += tmp
                flag = False
            if i == ")":
                tmp //= 2
            else:
                tmp //= 3
if len(stack) or summary == 0:
    print(0)
else:
    print(summary)
