test_Case = int(input())
for i in range(test_Case):
    N,M = map(int,input().split())
    papers = list(map(int,input().split()))


    cnt = 0
    while len(papers) != 0:
        if papers[0] == max(papers):
            papers.pop(0)
            cnt += 1
            if M == 0:
                print(cnt)
                break
        else:
            papers.append(papers.pop(0))
        if M == 0:
            M = len(papers)-1
        else:
            M -= 1
