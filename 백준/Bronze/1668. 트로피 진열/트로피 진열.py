N = int(input())
tropys = list(int(input())for _ in range(N))
left_max = 0
left_cnt = 0
for i in range(N):
    if tropys[i] > left_max:
        left_cnt += 1
        left_max = tropys[i]

right_max = 0
right_cnt = 0
for i in range(N-1,-1,-1):
    if tropys[i] > right_max:
        right_cnt += 1
        right_max = tropys[i]
        
print(left_cnt)
print(right_cnt)
    