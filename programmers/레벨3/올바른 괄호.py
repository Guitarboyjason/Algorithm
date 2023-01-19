from collections import deque

#
#
# def solution(s):
#     count = 0
#     if s.count(")") != s.count("("):
#         return False
#     while s:
#         if len(s) == 1 and count == 1 and s[0] == ")":
#             return True
#         elif len(s) == 1 and count > 1 or len(s) == 1 and s[0] == "(":
#             return False
#         if count == 0 and s[0] == ")":
#             return False
#         if s[0] == "(":
#             count += 1
#         if s[0] == ")":
#             count -= 1
#         s = s[1:]
#
#     return True
#
# s = ")()("
# print(solution(s))


def solution(s):
    stack = deque()
    for i in s:
        print(stack)
        print(len(stack))
        if i == "(":
            stack.append(i)
        if i == ")":
            if len(stack) == 0:
                return False
            stack.popleft()
    if len(stack) == 0:
        return True
    else:
        return False

