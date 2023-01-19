def solution(s):
    sign = 0;
    count = 0;
    for i in range(len(s)):
        if sign == 0 and s[i] == ")":
            return "false"
        elif sign == 1 and s[i] == ")" and count == 0:
            return "false"
        if s[i] == "(":
            sign = 1
            count += 1
        if s[i] == ")":
            if count > 0:
                count -= 1
                if count == 0:
                    sign = 0
    if sign == 1:
        return "false"
    return "true"


s = ")()("
print(solution(s))