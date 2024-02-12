n_questions = int(input())
# possible = {1:[],2:[],3:[]}

possible = {i:[] for i in range(1,10)}
answer = 0
for _ in range(n_questions):
    question,strike,ball = map(int,input().split())
    if strike ==3 :
        answer = 1
    if answer or not(strike + ball):      # 이미 3strike가 나온 경우, ball과 strike가 모두 0인 경우
        continue
    if 