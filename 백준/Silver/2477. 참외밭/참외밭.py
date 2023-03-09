#2477-참외밭.py

#사각형의 면적을 구하는것이 최 우선임.
#그럼 가장 크게 테두리를 그린 뒤 찌그러진 모양만큼 빼주는건 어떨까

## 아니면 
import sys
K = int(sys.stdin.readline())

dic = {4:2,2:3,3:1,1:4}
# case 1: 진행 잘 하다 이 dic에 포함 되지 않는 부분을 발견 할 경우
#   발견 한 당시와 그 다음 차례를 확인하여 그 곱만큼 뺀다

# case 2: 진행 하자마자 확인하는경우
#   1과 동일

# case 3: 진행하는데 확인이 안되는 경우
#   처음과 마지막 진행을 확인하여 그 곱만큼 뺀다.

arr = []
row=[]
column = []
for i in range(6):
    arr.append(list(map(int,input().split())))

for i in arr:
    if i[0] == 1 or i[0] == 2:
        row.append(i)
    else:
        column.append(i)

sign = 0
# print(max(row),max(column))
len_sum = max(row,key=lambda x : x[1])[1] * max(column,key=lambda x : x[1])[1]
for i in range(5):
    if dic[arr[i][0]] != arr[i+1][0]:
        sign = 1
        len_sum -= arr[i][1] * arr[i+1][1]
if not sign:
    len_sum -= arr[0][1] * arr[-1][1]
print(len_sum * K)
    