#11478-서로다른부분문자열의개수.py

import sys
S = sys.stdin.readline().rstrip()
tmp = set()
for i in range(len(S)+1):
    for j in range(i):
        tmp.add(str(S[j:i]))

print(len(tmp))