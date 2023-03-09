# 1
# 1 - 3

# 2
# 1 - 2
# 1 - 3
# 2 - 3

# 3
# 1 - 3     # 2와 3을 swap
# 1 - 2
# 3 - 2
# 1 - 3     # 3을 3에 옮김

# 2 - 1     # 2와 3을 swap
# 2 - 3
# 1 - 3


# 4
# 1 - 2     # 2 와 3 을 swap
# 1 - 3
# 2 - 3

# 1 - 2     # 여전히 2 와 3을 swap
# 3 - 1
# 3 - 2
# 1 - 2
# 1 - 3     # 4를 3으로 옮김

# 2 - 3     # 여기서부턴 3개의 과정을 2와 3을 swap한 것.

#
N = int(input())
def hanoi_problem(N):
    # if N == 1:
    #     return [[1,3]]
    if N == 1:
        return [[1,3]]
    if N == 2:
        return [[1,2],[1,3],[2,3]]
    else:
        tmp = hanoi_problem(N-1)
        ttmp = [0,0]
        may_hanoi = []
        for i in tmp:
            if i[0] == 1:
                ttmp[0] = 1
            elif i[0] == 2:
                ttmp[0] = 3
            else:
                ttmp[0] = 2
            if i[1] == 1:
                ttmp[1] = 1
            elif i[1] == 2:
                ttmp[1] = 3
            else:
                ttmp[1] = 2
            may_hanoi.append(ttmp)
            ttmp =[0,0]

        may_hanoi.append([1,3])
        for i in tmp:
            if i[0] == 1:
                ttmp[0] = 2
            elif i[0] == 2:
                ttmp[0] = 1
            else:
                ttmp[0] = 3
            if i[1] == 1:
                ttmp[1] = 2
            elif i[1] == 2:
                ttmp[1] = 1
            else:
                ttmp[1] = 3
            may_hanoi.append(ttmp)
            ttmp =[0,0]

        return may_hanoi
answer = hanoi_problem(N)
print(len(answer))
for i in answer:
    print(i[0], i[1])
