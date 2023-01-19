import re

def solution(s):
    if s.isdigit() and len(s) in (4,6):
        return True
    return False

print(solution("1001"))
