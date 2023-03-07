# 이동하려는 채널 N
# 고장난 버튼의 개수 M
# N중에서 몇가지의 숫자가 고장이 났나
# 부러지지 않은 숫자들 중 N과 가장 가까운 수를 구하면 될 것.
# 특이 케이스 : broken = [9], 99999 -> 100_000
#            broken = [0], 0    -> 1
# 부러지지 않은 숫자들과 겹치는 수를 구한다면?
# 그 수들은 무조건 고정일까?

# N = 99998, broken = [9], 8이 고정이 아니다. 100_000로 가는게 나음
# 이동하려는 채널의 범위가 500_000임
# 이러면 나올 수 있는 수의 범위가 최대 500_000*2-100 정도
# 이후로 넘어가면 100에서 출발하는거랑 별 차이가 없음
import heapq
import sys
sys.stdin = open("baekjoon/input.txt","r")

N = int(input())
M = int(input())
if M:
    broken_buttons = list(map(int,input().split()))
else:
    broken_buttons = []
now = 100
channels = [True]*(N+abs(N-now)+1)

if broken_buttons:
    for channel in range(len(channels)):
        for b_button in broken_buttons:
            if str(b_button) in str(channel):
                # print(1)
                channels[channel] = False
                break

tmp = [abs(index-N)+len(str(index)) for index,i in enumerate(channels) if i == True]
if tmp:
    heapq.heapify(tmp)
    print(min(abs(N-now),tmp[0]))
else:
    print(abs(N-now))    