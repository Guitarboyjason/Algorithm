

#dic으로 구현하면 빨리 나오겠다

def solution(n,words):
    done = dict()
    for index, i in enumerate(words):

        if i in done or index != 0 and words[index-1][-1] != i[0]:
            return [(index)%n+1,(index)//n+1]
        done[i] = index
    return [0,0]
n = 3
words =["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n,words))
