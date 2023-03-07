# def hamberger(level):
#     if level == 0:
#         return "P"
#     return "B"+hamberger(level-1) + "P" + hamberger(level-1)+"B"
# N,X = map(int,input().split())
# print(hamberger(N)[:X].count("P"))

N,X = map(int,input().split())
dp_b = [-1] *(N+1)
dp_b[0] = 1
for i in range(1,N+1):
    dp_b[i] = dp_b[i-1]*2+3
    
dp_p = [-1]*(N+1)
dp_p[0] = 1
for i in range(1,N+1):
    dp_p[i] = dp_p[i-1]*2+1
    
p_cnt = 0
# X-= N # 버거 번만 먹은 숫자
for burger_index in range(N,-1,-1):
    ## 마지막꺼 처리 해줘야함
    if dp_b[burger_index]//2 >= X:
        # p_cnt += dp_p[burger_index]
        X -= dp_b[burger_index] // 2
        