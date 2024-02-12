# 모든 캣닢이 살아있는 기간이 최대한 길어지도록 물을 준다. 첫 캣닢이 죽는 날짜?
# 그럼 수분이 가장 적은 화분에 물을 줘야겠네, 근데 연속된 A개의 화분에 물을 준다....
# 연속된이 안겹치도록 물을 줄 때를 확인해보자
N,K,A,B = map(int,input().split())
cycle = N//A+1 if  N / A != N // A else N//A
cnt = 0
cnt_cycle = 0
while K >0:
    K -= 1
    cnt_cycle += 1
    if cnt_cycle == cycle:
        K += B
        cnt_cycle = 0
    cnt += 1
print(cnt)