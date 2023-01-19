#어렵지 않아보이는데..?

def solution(genres,plays):
    answer = []
    genr_play_cnt = set(i for i in genres)
    old_genr_play_cnt = list(genr_play_cnt)
    genr_play_cnt = dict()
    for i in range(len(old_genr_play_cnt)):
        genr_play_cnt[old_genr_play_cnt[i]] = 0
    for index,i in enumerate(genr_play_cnt):
        for jndex,j in enumerate(genres):
            if i == j:
                genr_play_cnt[i] +=  plays[jndex]

    arr = [[i,plays[index],genr_play_cnt[i],-index] for index,i in enumerate(genres)]
    print(arr)
    arr.sort(key=lambda x:(x[2],x[1],x[3]),reverse=True)
    print(arr)
    for i in genr_play_cnt:
        genr_play_cnt[i] = 0
    for i in arr:
        if genr_play_cnt[i[0]] != 2:
            genr_play_cnt[i[0]] += 1
            answer.append(-i[3])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres,plays))
