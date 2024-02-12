#k개의 접시를 연속해서 먹을 경우 할인된 가격
#1번 행사에 참여할 경우 쿠폰에 적힌 조류의 초밥 하나를 추가로 무료로 제공
#       현재 벨트에 없을 경우 새로 만들어 제공
#가능한 다양한 종류의 초밥을 먹을 것.

# 벨트 상태, 초밥의 가짓수, 연속해서 먹는 접시의 개수, 쿠폰 번호
# 손님이 먹을 수 있는 초밥 가짓수의 최댓값

N,d,k,c = map(int,input().split())
sushi = [int(input())for _ in range(N)]
sushi += sushi[:k-1]
maximum = -1

for i in range(N):
    pos = sushi[i:i+k]
    pos.append(c)
    cnt = len(set(pos))
    if maximum < cnt :
        maximum = cnt
    if maximum == d:
        break
print(maximum)