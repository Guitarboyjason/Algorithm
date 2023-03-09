import sys
input = sys.stdin.readline

N,K = map(int,input().split())
arr_N = []
for _ in range(N):
    arr_N.append(list(map(int,input().split())))
time_summary = 0
money_summary = 0

def find_best_worth(index, money,time):
    if time > K:
        return -1
    if index == N:
        return money
    return max(find_best_worth(index+1,money+arr_N[index][1],time+arr_N[index][0]),
               find_best_worth(index+1,money+arr_N[index][3],time+arr_N[index][2]))

print(find_best_worth(0,0,0))

