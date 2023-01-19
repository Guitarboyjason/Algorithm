def solution(quiz):
    correct = []
    sign = 1
    a = ""
    b = ""
    answer = ""
    for j in quiz:
        for i in j :
            if i != " ":
                if i == "=":
                    sign = 2
                    continue
                elif i in ["+","-"]:
                    b += i
                    sign = 0
                    continue
                elif sign == 1:
                    a += i
                elif sign == 0:
                    b += i
                else:
                    answer += i
        print(a,b,answer)
        if (int(a) + int(b) == int(answer)):
            correct.append("O")
        else:
            correct.append("X")
    return correct

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
