#1620-나는야포켓몬마스터이다솜.py
import sys
import re
# input = sys.stdin.readline

N,M = map(int, sys.stdin.readline().split())
answer = {}
pattern = r"^[0-9]"
for i in range(N):
    answer[i+1] = sys.stdin.readline().rstrip()
answer_swaped = {v:k for k,v in answer.items()}
for i in range(M):
    question = sys.stdin.readline().rstrip()
    try:
        print(answer[int(question)])
    except:
        print(answer_swaped[question])


