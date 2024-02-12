'''
한 열의 램프를 토글
한 행에 있는 램프가 모두 켜져있을 때 행이 켜져있다고 한다.
K번 누를 것
서로 다른 K개를 누를 필요는 없다.
켜져있는 행을 최대로 하려 한다.

'''
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

lamps = [input() for _ in range(N)]
K = int(input())
# print(lamps)

# 최적의 상태를 얻기 위해 브루트포스?
# 최적의 상태란 행이 켜질 수 있는 최대한 켜졌을 때
# 하나의 행에 1과 0의 갯수 보면 해당 보드에서 나올 수 있는 최대한의 켜진 행 갯수를 알 수도
# 0을 가장 많이 가진 행을 뒤집는다?

# 실제로 뒤집을 필요는 없는 것 같고 해당 행이 뒤집혔는지 아닌지를 저장하고 있으면 될 것 같긴해

# K 가 1000까지, N,M은 50까지씩
# 그럼 K번 선택할 수 있는 가장 큰 경우의 수는 50**1000이 되겠다.
# 근데 사실상 50 ** 50 정도로도 충분하긴해 순서는 중요치 않다.

# 50C50전까지..?

# 그냥 똑같은게 몇번 나오냐 이말인 것 같아

# 저장할 때 (나오는 갯수, 패턴) 으로 저장
# 나오는 갯수대로 내림차순으로 정렬
# for문으로 돌면서 해당 패턴에 들어가있는 (K - 0의 갯수)% 2 == 0 이면 나오는 갯수를 출력
# 마지막까지 출력 못하면 0을 출력

patterns = dict()
for row in lamps:
    if row in patterns:
        patterns[row] += 1 
    else:
        patterns[row] = 1

pattern_list = []
for key,value in patterns.items():
    pattern_list.append([value,key])

pattern_list.sort(reverse=True)

for cnt, pattern in pattern_list:
    tmp = pattern.count('0')
    if (K-tmp)%2 == 0:
        print(cnt)
        break
else:
    print(0)

