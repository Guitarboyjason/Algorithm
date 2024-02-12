# 순서 바꾸기 x
# w대의 트럭만 동시에 올라갈 수 있다.
# 하나의 단위시간에 하나의 단위 길이만큼만 이동
# 무게의 합은 L보다 작거나 같아야 한다.
# 

from collections import deque
import sys
input = sys.stdin.readline

n_truck,len_bridge,max_weight = map(int,input().split())
weight_trucks = deque(map(int,input().split()))

bridge = deque()
cnt = 0
while weight_trucks:
    c_truck = weight_trucks.popleft()
    while True:
        cnt += 1
        finishied = False
        if bridge:
            for truck in bridge:
                truck[1] -= 1   # 남은 거리 -1
                if truck[1] == 0:
                    finishied = True
        if finishied:
            bridge.popleft() # 어차피 제일 앞이다
                    
        if sum(i[0] for i in bridge) + c_truck <= max_weight:
            bridge.append([c_truck,len_bridge])
            break
cnt += len_bridge
print(cnt)