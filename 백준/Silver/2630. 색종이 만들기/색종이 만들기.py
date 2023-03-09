import sys

def cnt_papers_white_blue(papers):
    n = len(papers)
    if n == 1:
        if papers[0][0] == 0:
            return [1,0]
        else:
            return [0,1]
    else:
        tmp = set()
        for j in [list(set(i))for i in papers]:
            tmp = set(list(tmp) + j)
        
        if len(tmp)== 1:
            if papers[0][0] == 0:
                return [1,0]
            else:
                return [0,1]
        else:
            return_value = [0,0]
            for i in range(2):
                for j in range(2):
                    white,blue = cnt_papers_white_blue([paper[n//2*j:n//2*(j+1)] for paper in papers[n//2*i:n//2*(i+1)]])
                    return_value[0] += white
                    return_value[1] += blue
            return return_value

N = int(input())
papers = [list(map(int,input().split()))for _ in range(N)]

for i in cnt_papers_white_blue(papers):
    print(i)