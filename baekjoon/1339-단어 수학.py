#무조건 높은 위치에 있는 단어에 9를 줘선 안된다.

# AAA
#  BB
#  BB
#  BB
#  BB

# 가 되면 B에 9를 주고 A에 8을 주는 편이 더 크다.
# 그럼 결국 패턴을 구해야 하나..

layer = [[] for _ in range(8)]
N = int(input())
nums = [input() for _ in range(N)]
for num in nums:
    num = num[::-1]
    for index in range(len(num)-1,-1,-1):
        layer[index].append(num[index])
print(layer)