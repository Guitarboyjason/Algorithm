# # 자신의 키가 몇 번째인지 알 수 있는 학생들이 모두 몇명인지 계산하여 출력하는 프로그램

# # 그래프 상으로 연결되어 있는 사람을 계산한다면 가능할지도
# # 시간 복잡도가 중요할 것 같은데 N <= 500, 대략 M<=N^2
# # 그럼 N 만큼 확인을 하려면 얼추 N^3 정도 되나
# # 시간이 애매한데
# # 그럼 현재까지 연결돼있는 사람의 수를 저장해두면 어떨까

from pprint import pprint
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
relations = [[0]*N for _ in range(N)]
# print(relations)

for _ in range(M):  # 관계 업데이트
    small,tall = map(int,input().split())
    relations[small-1][tall-1] = 1
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            if relations[i][k] == 1 and relations[k][j] == 1:
                relations[i][j] = 1
pprint(relations)
answer = 0
for i in range(N):
    checker = 0
    for j in range(N):
        checker += relations[i][j] + relations[j][i]
    if checker == N-1:
        answer += 1
print(answer)