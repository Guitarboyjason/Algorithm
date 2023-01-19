from collections import deque
# 짝지어 있는 문자들을 제거하고 모두 제거되면 종료
# 성공적으로 수행할 수 있는지 반환
# 문자열의 길이가 1000000 이므로 두번 while문을 돌렸다가는 시간초과가 나올 것

def solution(s):
    #전처리 먼저
    if len(s) % 2 ==1:
        return 0
    stack = deque()
    for i in s:
        if len(stack) != 0 and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) != 0:
        return 0
    return 1


    # while(s):
    #     tmp = s
    #     for i in range(len(s)-1):
    #         if s[i] == s[i+1]:
    #             s = s[:i] + s[i+2:]
    #             break
    #     if s == tmp:
    #         return 0
    # return 1

print(solution("baabaa"))
