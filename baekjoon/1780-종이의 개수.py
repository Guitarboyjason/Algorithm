import sys
sys.stdin = open("baekjoon/input.txt","rt")

N = int(input())
paper = [list(map(int,input().split()))for _ in range(N)]

def cut_papers(paper):
    n = len(paper)
    
    # if n == 1:
    #     return 
    # else:
    tmp = []
    for j in [list(set(i)) for i in paper]:
        tmp.extend(j)
        
    if len(set(tmp)) == 1:
        paper_to_return = [0,0,0]
        
        paper_to_return[tmp[0]+1] += 1
        return paper_to_return
    else:
        pieces_to_return = [0,0,0]
        for i in range(3):
            for j in range(3):
                for kndex,k in enumerate(cut_papers([piece[n//3*j:n//3*(j+1)] for piece in paper[n//3*i:n//3*(i+1)]])):
                    pieces_to_return[kndex] += k
        return pieces_to_return
# print(cut_papers(paper))
for printer in cut_papers(paper):
    print(printer)