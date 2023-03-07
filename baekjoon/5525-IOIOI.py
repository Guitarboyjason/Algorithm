import re

N = int(input())
M = int(input())
S = input().strip("O")
cnt = 0
for i in range(M,N-1,-1):
    compare = "IO"*(i//2+1)+"I"
    if len(compare) > len(S):
        continue
    if S.find(compare) != -1:
        cnt += (len(re.findall(compare,S)))
        # for i in re.findall(compare,S):
        S = S.replace(compare,"")
        # S = S[:]
print(cnt)