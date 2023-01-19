import re
def solution(str1,str2):
    p = re.compile(str2)
    if p.search(str1):
        return 1
    else:
        return 2
p = re.compile("6CD")
m = p.search("ab6CDE443fgh22iJKlmn1o")
print(m)
print(solution("ab6CDE443fgh22iJKlmn1o","6CD"))
