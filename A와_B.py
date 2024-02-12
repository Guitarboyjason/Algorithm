'''
S를 T로 바꾼다.
- 문자열의 뒤에 A를 추가한다
- 문자열을 뒤집고 뒤에 B를 추가한다.

첫째줄에 S
둘째줄에 T

S를 T로 바꿀 수 있으면 1, 없으면 0을 출력한다.

바꿀 수 없는 경우
1. T안에 S가 없는 경우
1-1. 단 뒤집어서 포함이 될 수도 있다.
2. 포함돼있다고 하더라도 바로 뒤에 B가 포함되는 경우나 앞에 A가 붙는 경우
2-2. 뒤집에서 포함이 된 경우엔 바로 뒤에 B가 붙어도 됨

예 )
S = AB
T = AAABBB
    AAABBA
'''

# 아니면 S를 기준으로 왼쪽과 오른쪽으로 나눠
# 나눴을 때 
#   1. 뒤집지 않은 경우, 앞에 A, 뒤에 B가 먼저 오면 안된다.
#   2. 뒤집은 경우, 앞에 B, 뒤에 A가 먼저 오면 안된다. 그리고 마지막에는 무조건 B가 들어가야함.



# 사실 A가 연속되는 부분은 A하나로 퉁쳐도돼.
# 근데 굳이..?


from collections import deque
import sys

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

# answer = 0
# if S not in T and S[::-1] not in T:
#     pass

# else:
#     if S in T:
#         # tmp = T.split(S)
flag_reversed = False
T = deque(T)
answer = 0
while T:
    # print("".join(T))
    if not flag_reversed and "".join(T) == S or flag_reversed and "".join(reversed(T)) == S:
        answer = 1
        break
    
    if not flag_reversed:# 정방향인경우 뒤에 A가 나와도 된다.
        if T[-1] == "A":
            T.pop()
        else:
            T.pop()
            flag_reversed = True
    else:
        if T[0] == "A":
            T.popleft()
        else:
            T.popleft()
            flag_reversed = False
        
print(answer)