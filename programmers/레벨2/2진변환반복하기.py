def solution(s):
    answer = [0,0]
    while(s != "1"):
        answer[0] += 1
        count = 0
        new_s = ""
        for i in s:
            if i == "0":
                count += 1
            else:
                new_s += i
        answer[1] += (count)
        c = len(new_s)
        new_s = ""
        while(c):
            new_s += str(c%2)
            c = c//2
        
        # s =reversed(new_s)
        s = new_s[::-1]

    return answer

print(solution("110010101001"))