'''
각 위치에서 가장 가까운 네잎클로버를 찾는다..
이분탐색으로 풀건데 탐색하는 기준을 뭘로 잡지

'''
import sys
input = sys.stdin.readline
N,M = map(int,input().rstrip().split())

x_dict= dict()  # 같은 x들을 저장
y_dict = dict() # 같은 y들을 저장
for _ in range(N):
    x,y = map(int,input().rstrip().split())
    if x not in x_dict:
        x_dict[x] = [y]
    else:
        x_dict[x].append(y)
    if y not in y_dict:
        y_dict[y] = [x]
    else:
        y_dict[y].append(x)

for i in x_dict:
    x_dict[i].sort()
    
for i in y_dict:    #정렬이 필요함
    y_dict[i].sort()
    
    
now_x,now_y = 0,0   # 계속 확인할 좌표
command = input().rstrip()

for c in command:
    if c == "U" or c == "D":
        idx_y = False
        start = 0
        end = len(x_dict[now_x])
        # 그냥 x,y를 찾으면 되는거 아닌가
        
        while start <= end:
            middle = (start+end) // 2
            if x_dict[now_x][middle] < now_y:
                start = middle + 1
            elif x_dict[now_x][middle] == now_y:
                if c == "U":
                    idx_y = middle + 1
                else:
                    idx_y = middle - 1
                break
            else:
                end = middle
                
        now_y = x_dict[now_x][idx_y]
    else:#x축이동
        idx_x = False
        start = 0
        end = len(y_dict[now_y])
        
        while start <= end:
            middle = (start+end) // 2
            if y_dict[now_y][middle] < now_x:
                start = middle + 1
            elif y_dict[now_y][middle] == now_x:
                if c == "R":
                    idx_x = middle + 1
                else:
                    idx_x = middle - 1
                break
            else:
                end = middle
                
        now_x = y_dict[now_y][idx_x]
print(now_x,now_y)