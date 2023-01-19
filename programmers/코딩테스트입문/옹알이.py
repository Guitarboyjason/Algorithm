def solution(babbling):
    can=["aya","ye","woo","ma"]
    for i in babbling:
        tmp = i
        index = -1
        while(tmp):
            for jndex,j in can:
                if j[0] == tmp[0]:
                    if tmp[:len(j)] == j and index == jndex:
                        


    return answer

print(solution(["aya", "yee", "u", "maa"]))
