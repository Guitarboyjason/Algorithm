emergency = [3, 76, 24]


def solution(emergency):
    tmp = [i for i in emergency]
    tmp.sort(reverse=True)
    # answer = [i for i in emergency ]
    answer = [tmp.index(i)+1 for i in emergency]
    # for i in answer:
    # answer = [ for i in answer]
    # answer = []
    # for i in emergency:
    #     print(i)
    #     for j in tmp:
    #         if i == j[1]:
    #             print(j)
    #             answer.append(j[0])
    return answer


print(solution(emergency))
